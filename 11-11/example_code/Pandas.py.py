import pandas as pd
dfs = pd.read_html("https://rate.bot.com.tw/xrt?Lang=zh-TW")
#取第一個表格 dfs[0](HTML可能含有多個表格)
currency = dfs[0]
#print(currency)


#取前五行
currency = currency.iloc[:,0:5]
#設定欄位名稱
currency.columns = [u'幣別', u'現金匯率(買入)', u'現金匯率(賣出)', u'即期匯率(買入)', u'即期匯率(賣出)']
#幣別使用英文代號，也就是在'('與')'之間的英文
currency[u'幣別'] = currency[u'幣別'].str.extract('\((\w+)\)')
print(currency)
'''
from datetime import datetime as dt
currency['Date'] = dt.now().strftime("%Y-%m-%d")
print("/"*150)
print(currency)
print("/"*150)
'''
import sqlite3

#將currency資料倒入currency.sqlite 資料庫的currency表格
with sqlite3.connect('C:\\Users\\Liu\\Desktop\\2024 Python\\8. Crawler\\currency.sqlite') as db:
    currency.to_sql('currency', con=db, if_exists='append')

with sqlite3.connect('C:\\Users\\Liu\\Desktop\\2024 Python\\8. Crawler\\currency.sqlite') as db:
    df = pd.read_sql_query('select * from currency', con=db)

print(df)
