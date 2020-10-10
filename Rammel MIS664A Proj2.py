# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:49:05 2020

@author: Mike Rammel MIS664A Project2
"""

import datetime
import mysql.connector
import sqlalchemy
from sqlalchemy import create_engine
import pandas_datareader.data as web

start = datetime.datetime(2010,9,22)
end = datetime.datetime(2020,9,22)


# tickerlist = ['aapl','amzn','mdb','msft','orcl','qqq','spy','tsla', 'ge', 'kodk', 'ibio', 
#               'rtx', 'vxrt', 'sne' ,'aal', 'ino', 'f', 'fb', 'amd', 'abev', 'spx']
tickerlist = ['aapl']
firstticker = 0

for ticker in tickerlist:
    stockdata = web.DataReader(ticker,'yahoo',start,end)
    # print(stockdata.keys())
    stockdata.sort_index(inplace=True)
    stockdata['Ticker'] = ticker
    stockdata['TradeDate'] = stockdata.index
    stockdata['OpenPrice'] = stockdata['Open']
    stockdata['HighPrice'] = stockdata['High']
    stockdata['LowPrice'] = stockdata['Low']
    stockdata['AdjClose'] = stockdata['Adj Close']
    stockdata['Close'] = stockdata['Close']
    stockdata['Volume'] = stockdata['Volume']
    # for c in stockdata['TradeDate']:
    #     print(c)
    x = len(stockdata['TradeDate'])
    i = 0
    while i < x:
        print(stockdata['TradeDate'][i])
    # stockdata2 = stockdata[['TradeDate', 'Ticker', 'OpenPrice','HighPrice','LowPrice','Close','AdjClose','Volume']]
    # stockdata2.columns = ['TradeDate', 'Ticker', 'OpenPrice','HighPrice','LowPrice','Close','AdjClose','Volume']
    # print(stockdata2.columns)
    
    # engine = create_engine('mysql+mysqlconnector://root:{}@127.0.0.1:3306/mydata'.format('samiran'), connect_args={'auth_plugin': 'mysql_native_password'})
    # stockdata2.to_sql(name=ticker, con=engine, if_exists = 'replace', index=False)
    # stockdata2.to_csv(ticker + '.csv')
    
    # print(ticker, ' done.') 
    
# print(stockdata2)
