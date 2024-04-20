import requests
import datetime
from bs4 import BeautifulSoup
#날짜
d = datetime.datetime.now()
month = d.month
day = d.day

# 네이버_삼성
url1 = "https://finance.naver.com/item/sise.naver?code=005930"
response = requests.get(url1)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
price1 = soup.select_one("#_nowVal").text   #id=# class=.
print("SAMSUNG:"+price1)
# 야후 파이낸스_애플
url2 = 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'
response = requests.get(url2)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
price2 = soup.select_one(".Fw\(b\).Fz\(36px\).Mb\(-4px\).D\(ib\)").text
print('AAPL:'+price2)
price2 = float(price2)
