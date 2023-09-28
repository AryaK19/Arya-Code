import pandas as pd
import pandas_datareader as web
import datetime as dt

File = "Listt"


def tickers_make_NS(tickers):
    for ticker in tickers:
        ticker_NS = ticker + '.NS'
        RSI(ticker_NS, Dict, ticker)


def RSI(ticker_NS, Dict, ticker):

    days = 14

    start = dt.datetime.now() - dt.timedelta(days=365)

    data = web.get_data_yahoo(ticker_NS, str(start))
    
    dataClose = data['Close'].iloc[-1]
    dataClose150 = data['Close'].iloc[-150]
    
    delta = data['Close'].diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    average_up = up.ewm(com=(days - 1), adjust=False).mean()
    average_down = down.ewm(com=(days - 1), adjust=False).mean()
    rs = average_up / average_down

    data['RSI'] = 100 - (100 / (1 + rs))

    data = data.iloc[-150:]

    data = data['RSI']
    datalast = data.iloc[-1]
    dataprev2 = data.iloc[-2]
    dataprev3 = data.iloc[-3]
    dataprev4 = data.iloc[-4]
    dataprev5 = data.iloc[-5]
   

    datalast = round(datalast, 2)
    dataprev2 = round(dataprev2, 2)
    dataprev3 = round(dataprev3, 2)
    dataprev4 = round(dataprev4, 2)
    dataprev5 = round(dataprev5, 2)

    Dict.update({str(ticker): [datalast, dataprev2,
                dataprev3, dataprev4, dataprev5, dataClose , dataClose150]})
    
   


def STOCKS(list):

    print("LOADING...Please wait")

    tickers_1 = []

    tickers_bse = []

    f = open(f'{list}.txt')
    data = f.read()
    tickers_bse = data.split('//')
    tickers_1 = tickers_bse[0].split(',')
    f.close()

    tickers_bse = tickers_bse[1].split(',')

    if len(tickers_1) != 0 and tickers_1[0] != '':
        tickers_make_NS(tickers_1)

    if len(tickers_bse) != 0 and tickers_bse[0] != '':
        for ticker in tickers_bse:
            ticker_BO = ticker + '.BO'
            RSI(ticker_BO, Dict, ticker)


Dict = {}
fordown = {}
STOCKS(File)

buy = []
sell = []
hold = []
nothold = []


Dict = dict(sorted(Dict.items(), reverse=True, key=lambda item: item[1][0]))

for key, value in Dict.items():
    if (value[0] >= 67.5) and ((value[0] < value[1] < value[2]) or (value[0] < value[2])):
        sell.append(f"{key} : {value[0]}")

    elif (value[0] <= 33.5) and ((value[0] > value[1] > value[2]) or (value[0] > value[2]) and (value[5] > value[6])):
        buy.append(f"{key} : {value[0]}")

    elif (value[0] < value[1] < value[2] < value[3] < value[4]) or (value[0] < value[1] < value[2] < value[3]) or (value[0] < value[1] < value[2]) or (value[0] < value[1] < value[2] < value[4]) or (value[0] < value[1] < value[3] < value[4]) or (value[0] < value[2] < value[3] < value[4]) or (value[1] < value[2] < value[3] < value[4]) or (value[0] < value[1] < value[3]) or (value[0] < value[2] < value[3]) or (value[0] < value[3] < value[4]) or (value[0] < value[1] < value[4]):

        nothold.append(f"{key} : {value[0]}")

    else:
        hold.append(f"{key} : {value[0]}")


if len(buy) > 1:
    buy.reverse()

length = []
length.append(len(buy))
length.append(len(sell))
length.append(len(hold))
length.append(len(nothold))
length.sort(reverse=True)

if length[0] > len(buy):
    var = length[0] - len(buy)
    for i in range(var):
        buy.append(" ")

if length[0] > len(sell):
    var = length[0] - len(sell)
    for i in range(var):
        sell.append(" ")

if length[0] > len(hold):
    var = length[0] - len(hold)
    for i in range(var):
        hold.append(" ")

if length[0] > len(nothold):
    var = length[0] - len(nothold)
    for i in range(var):
        nothold.append(" ")

stocks = {}
stocks.update({'    BUY       ': buy})
stocks.update({'    SELL       ': sell})
stocks.update({'    HOLD       ': hold})
stocks.update({'    DOWN       ': nothold})

stocks = pd.DataFrame(stocks)

stocks.index += 1
table = stocks.to_string()

file = open("Table.txt", 'w')
file.write(table)
print("\n")
print(table)
file.close()
