import pandas as pd
import quandl
import math
import datetime

df = quandl.get('WIKI/GOOGL')

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 500)

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

df['HL_PCT'] = (df['Adj. High']-df['Adj. Close'])/df['Adj. Close']*100

df['PCT_change'] = (df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']*100

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-9999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))
print(len(df))
print(df.ix[35])

df['label'] = df[forecast_col].shift(-forecast_out)

df.dropna(inplace=True)
print(df)
