import pandas as pd
import pandas_datareader as web
import datetime as dt


def STOCKS():
    run = True

    tickers_1 = ['RELAXO', 'PRINCEPIPE', 'MCDOWELL-N', 'TECHM',
                 'BERGEPAINT', 'POLYCAB', 'RELIANCE', 'AMARAJABAT']
    tickers_2 = ['ASIANPAINT', 'PIDILITIND', 'GRANULES',
                 'TATAMOTORS', 'TATAPOWER', 'LUXIND', 'LALPATHLAB', 'TARSONS']
    tickers_3 = ['HINDUNILVR', 'HDFCBANK', 'DEEPAKNTR', 'IEX',
                 'DIVISLAB', 'MARKSANS', 'WIPRO', 'SUMICHEM', 'MOTHERSON']
    tickers_4 = ['RADICO', 'ICICIBANK', 'ITC', 'HAVELLS', 'DMART']

    tickers_add = []

    tickers_bse = ['BLACKROSE']

    tickers_make_NS(tickers_1)
    tickers_make_NS(tickers_2)
    tickers_make_NS(tickers_3)
    tickers_make_NS(tickers_4)
    tickers_make_NS(tickers_add)
    
    if len(tickers_bse) != 0:
        for ticker in tickers_bse:
            ticker_NS = ticker+'.BO'
            RSI(ticker_NS, Dict, ticker)


def tickers_make_NS(tickers):
    for ticker in tickers:
        ticker_NS = ticker+'.NS'
        RSI(ticker_NS, Dict, ticker)


def RSI(ticker_NS, Dict, ticker):

    days = 14

    start = dt.datetime(2022, 1, 1)
    

    data = web.get_data_yahoo(ticker_NS, str(start))

    delta = data['Close'].diff()
    up = delta.clip(lower=0)
    down = -1*delta.clip(upper=0)
    average_up = up.ewm(com=(days - 1), adjust=False).mean()
    average_down = down.ewm(com=(days - 1), adjust=False).mean()
    rs = average_up/average_down

    data['RSI'] = 100 - (100/(1 + rs))

    data = data.iloc[days:]

    data = data['RSI']
    data = data.iloc[-1]

    data = round(data, 2)

    Dict.update({str(ticker): data})


Dict = {}
buy = []
sell = []
hold = []

STOCKS()

Dict = dict(sorted(Dict.items(), reverse=True, key=lambda item: item[1]))

for key, value in Dict.items():
    if value >= 70:
        sell.append(f"{key} : {value}")
    elif value <= 30:
        buy.append(f"{key} : {value}")
    else:
        hold.append(f"{key} : {value}")

buy.reverse()

length = []
length.append(len(buy))
length.append(len(sell))
length.append(len(hold))
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


stocks = {}
stocks.update({'BUY': buy})
stocks.update({'SELL': sell})
stocks.update({'HOLD': hold})

stocks = pd.DataFrame(stocks)

print(stocks)

stocks.to_excel('RSI.xlsx')
