import requests
from bs4 import BeautifulSoup
import datetime

#날짜
d = datetime.datetime.now()
date = str(d.month) +'/'+ str(d.day)
print('day:'+date)

#AAPL
url1 = 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'
response = requests.get(url1)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
price1 = soup.select_one(".Fw\(b\).Fz\(36px\).Mb\(-4px\).D\(ib\)").text
print('AAPL:'+price1)
price1 = float(price1)

#EDV
url2 = 'https://finance.yahoo.com/quote/EDV?p=EDV&.tsrc=fin-srch'
response = requests.get(url2)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
price2 = soup.select_one(".Fw\(b\).Fz\(36px\).Mb\(-4px\).D\(ib\)").text
print('EDV:'+price2)
price2 = float(price2) #텍스트->실수

#AAPL+EDV
total_price = price1+price2
print('total:', total_price)

#데이터 저장
out = open('date', 'a')
print(date, file=out)
out.close()

out = open('AAPL+EDV', 'a')
print(total_price, file=out)
out.close()
