import datetime
import requests
from bs4 import BeautifulSoup

#날짜
d = datetime.datetime.now()
date = str(d.month) +'/'+ str(d.day)
print('day:'+date)

#AAPL40%
url1 = 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'
response = requests.get(url1)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
price1 = soup.select_one(".Fw\(b\).Fz\(36px\).Mb\(-4px\).D\(ib\)").text
price1 = float(price1)
price1 = price1*4
print('AAPL40%:', price1)

#IEF20%
url2 = 'https://finance.yahoo.com/quote/IEF?p=IEF&.tsrc=fin-srch'
response = requests.get(url2)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
price2 = soup.select_one(".Fw\(b\).Fz\(36px\).Mb\(-4px\).D\(ib\)").text
price2 = float(price2)
price2 = price2*2
print('IEF20%:', price2)

#TLT40%
url3 = 'https://finance.yahoo.com/quote/TLT?p=TLT&.tsrc=fin-srch'
response = requests.get(url3)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
price3 = soup.select_one(".Fw\(b\).Fz\(36px\).Mb\(-4px\).D\(ib\)").text
price3 = float(price3)
price3 = price3*4
print('TLT40%:', price3)

#total
total_price = price1 + price2 + price3
print('total:', total_price)

#데이터저장
out = open('day','a')
print(date, file=out)
out.close()

out = open('price','a')
print(total_price, file=out)
out.close()

import matplotlib.pyplot as plt
import numpy as np

#데이터불러오기
testfile = open('day','r')
day = testfile.readlines() #리스트로 읽음

testfile = open('price','r')
price = testfile.readlines() #리스트로 읽음

prices = list(map(float, price)) #리스트->실수

#그래프
x = np.arange(len(day)) 
plt.bar(x, prices)
plt.xticks(x, day)
plt.bar(x, prices, width=0.8)

plt.bar(x,prices)  #막대그래프 위에 값표시
for i, v in enumerate(x):
    plt.text(v, prices[i], prices[i],                 
             fontsize = 9, 
             color='blue', 
             horizontalalignment='center', 
             verticalalignment='bottom')   
plt.show()