import mysql.connector
import datetime
import sqlalchemy
from sqlalchemy import create_engine
import pandas_datareader.data as web

my_db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'samiran',
    database='mydata'
)
my_cursor = my_db.cursor(buffered=True)
# my_cursor.execute("CREATE DATABASE mydata")
my_cursor.execute("USE mydata")
try:
    # exception handling and creating tables at the first time.
    stock = "CREATE TABLE IF NOT EXISTS Stock(StockKey INT NOT NULL  AUTO_INCREMENT PRIMARY KEY, StockTicker TEXT(5), StockName VARCHAR(45))"
    date = "CREATE TABLE IF NOT EXISTS Date(DateKey INT AUTO_INCREMENT NOT NULL PRIMARY KEY, Date DATE, IsWeekend TINYINT, IsHoliday TINYINT)"

    stockFact = "CREATE TABLE IF NOT EXISTS stockfact(Date_DateKey INT, Stock_StockKey INT, OpenPrice DECIMAL(6,2), HeighPrice DECIMAL(6,2), LowPrice DECIMAL(6,2), ClosePrice DECIMAL(6,2), DailyPerformance DECIMAL(6,4), DailyComp DECIMAL(7,4), MonthlyPerformance DECIMAL(6,4), FOREIGN KEY(Date_DateKey) references date(datekey), FOREIGN KEY(Stock_StockKey) REFERENCES stock(stockkey));"
except: 
    pass


start = datetime.datetime(2010,9,22)
end = datetime.datetime(2020,9,27)
def load_data_to_mysql():
    # data

    tickerlist = ['aapl','amzn','mdb','msft','orcl','qqq','spy','tsla', 'ge', 'kodk', 'ibio',
                  'rtx', 'vxrt', 'sne' ,'aal', 'ino', 'f', 'fb', 'amd', 'abev', 'spx']
    firstticker = 0
    date_store = False
    for ticker in tickerlist:
        sql = "INSERT INTO stock (StockTicker, StockName) VALUES (%s, %s)"
        val = (ticker, ticker)
        my_cursor.execute(sql, val)
        my_db.commit()

    for ticker in tickerlist:
        # data of the ticker
        stockdata = web.DataReader(ticker,'yahoo',start,end)
        stockdata.sort_index(inplace=True)
        stockdata['Ticker'] = ticker
        stockdata['TradeDate'] = stockdata.index
        stockdata['OpenPrice'] = stockdata['Open']
        stockdata['HighPrice'] = stockdata['High']
        stockdata['LowPrice'] = stockdata['Low']
        stockdata['AdjClose'] = stockdata['Adj Close']
        stockdata['Close'] = stockdata['Close']
        stockdata['Volume'] = stockdata['Volume']

        counters=len(stockdata['TradeDate'])
        # inserting ticker value to stock table
        

        sql_date = "INSERT INTO Date (Date, IsWeekend, IsHoliday) VALUES (%s, %s, %s)"
        stockFacts = "INSERT INTO stockfact (Date_DateKey, Stock_StockKey, OpenPrice, HeighPrice, LowPrice, ClosePrice, DailyPerformance, MonthlyPerformance ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        query = "SELECT StockKey from stock where StockTicker=" + ticker
        my_cursor.execute(query)
        stock_id = my_cursor.fetchall()
        print(stock_id[0][0])
        today_date = start
        i = 0
        print(counters)
        while i < counters:
            # itiration for storing the individual data to db
            # print(i)
            if date_store == False:
                x=stockdata['TradeDate'][i]

                isHoliday = False
                isWeekend = False
                date = stockdata['TradeDate'][i].strftime('%Y-%m-%d %H:%M:%S')
                vals =(date, isHoliday, isWeekend)
                my_cursor.execute(sql_date, vals)
                my_db.commit()

                my_cursor.execute("SELECT last_insert_id()")
                date_id = my_cursor.fetchall()
            else:
                query2 = "SELECT datekey in date WHERE date="+ stockdata['TradeDate'][i]
                my_cursor.execute(query2)
                date_id = my_cursor.fetchall()
            dayPerformance = (stockdata['High'][i] - stockdata['Low'][i])/ stockdata['Volume'][i]
            MonthlyPerformance = 0
            vals_stockfact = (date_id[0][0], stock_id[0][0], stockdata['Open'][i], stockdata['High'][i], stockdata['Low'][i], stockdata['Close'][i], dayPerformance, MonthlyPerformance)
            my_cursor.execute(stockFacts, vals_stockfact)
            my_db.commit()
            today_date = today_date + datetime.timedelta(days=1)
            i=i+1
        date_store = True
        print(ticker, ' done.')

# load_data_to_mysql()
    
# print(stockdata2)

# Queston4.a
# my_cursor.execute("SELECT DISTINCT StockTicker from Stock")
# security = my_cursor.fetchall()
# print(security)
#
# # Question4.b>:==>
# my_cursor.execute("SELECT closeprice from stockfact WHERE date_datekey = (SELECT datekey FROM date WHERE date = '2020-07-01') AND stock_stockkey IN (SELECT stockkey FROM stock WHERE stockticker IN (SELECT DISTINCT stockticker FROM stock));")
# close_price = my_cursor.fetchall()


# Question 4.d:==>
'weekend'

# Question 4.e:==>
today_dates = end
yesterday_dates = end - datetime.datetime.fromtimestamp(days=1)
print(yesterday_dates)