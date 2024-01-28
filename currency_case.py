# -*- coding: utf-8 -*-

import pandas as pd
import datetime
from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2021, 1, 1)
end_date = date(2021, 1, 10)

df = pd.DataFrame()
for single_date in daterange(start_date, end_date):
    dfs = pd.read_html(f'https://www.xe.com/currencytables/?from=USD&date={single_date.strftime("%Y-%m-%d")}')[0]
    dfs['Date'] = single_date.strftime("%Y-%m-%d")
    df = df.append(dfs)

df_usd = df.drop(df.columns[[1, 3]],axis = 1)
columns = ['Date', 'Currency', 'Units per USD']
df_usd = df_usd[columns]
df_usd.to_csv('exchange_rate_usd.csv')

df_usd.head()