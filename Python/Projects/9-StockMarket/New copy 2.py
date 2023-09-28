import pandas as pd
import pandas_datareader as web
import datetime as dt


start = dt.datetime.now() - dt.timedelta(days=1)
data = web.get_components_yahoo("TATAMOTORS.NS")

print(data)