import requests
from bs4 import BeautifulSoup
import datetime
import matplotlib.pyplot as plt
import numpy as np


#날짜
d = datetime.datetime.now()
date = str(d.month) +'/'+ str(d.day)
print('day:'+date)

#종목1
name1 = input('종목1명:')
url1 = 'https://finance.yahoo.com/quote/'+name1+'?p='+name1+'&.tsrc=fin-srch'
response = requests.get(url1)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
price1 = soup.select_one(".Fw\(b\).Fz\(36px\).Mb\(-4px\).D\(ib\)").text
print(name1+':'+price1)
price1 = float(price1)

#종목2
name2 = input('종목2명:')
url2 = 'https://finance.yahoo.com/quote/'+name2+'?p='+name2+'&.tsrc=fin-srch'
response = requests.get(url2)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
price2 = soup.select_one(".Fw\(b\).Fz\(36px\).Mb\(-4px\).D\(ib\)").text
print(name2+':'+price2)
price2 = float(price2) #텍스트->실수

#종목1+종목2
total_price = price1+price2
print('total:', total_price)

#데이터 저장
out = open('날짜','a')
print(date, file=out)
out.close()

out = open('입력값','a')
print(total_price, file=out)
out.close()

#파일불러오기
testfile = open('날짜','r')
day = testfile.readlines() #리스트로 읽음
# print('day:', day)

testfile = open('입력값','r')
price = testfile.readlines() #리스트로 읽음
# print('AAPL+EDV:', price)

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


