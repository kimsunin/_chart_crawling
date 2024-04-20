import matplotlib.pyplot as plt
import numpy as np
import requests
import datetime
from bs4 import BeautifulSoup

#날짜
d = datetime.datetime.now()
date = str(d.month)+"/"+str(d.day) #숫자를 문자로 변환
print(date)

#삼성
url1 = "https://finance.naver.com/item/sise.naver?code=005930"
response = requests.get(url1)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
price1 = soup.select_one("#_nowVal").text
price1 = int(price1.replace(',',''))
price1 = price1*3
print("삼성30%:", price1)

#sk하이닉스
url2 = "https://finance.naver.com/item/sise.naver?code=000660"
response = requests.get(url2)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
price2 = soup.select_one("#_nowVal").text
price2 = int(price2.replace(',',''))
price2 = price2*7
print("sk하이닉스70%:", price2)
total_price = price1 + price2
print("삼성+sk:", total_price)

#그래프
days = []
prices = []
if date not in days:
    days.append(date)
    prices.append(total_price) #왜 if문을 쓰지?

# x = np.arange(len(days))
# plt.bar(x, prices)
# plt.xticks(x, days)
# plt.bar(x, prices, width=0.8)

# plt.bar(x,prices)  #막대그래프 위에 값표시
# for i, v in enumerate(x):
#     plt.text(v, prices[i], prices[i],                 
#              fontsize = 9, 
#              color='blue', 
#              horizontalalignment='center', 
#              verticalalignment='bottom')    
# plt.show() 

#데이터저장
out = open('','a')
print(total_price, file=out)
out.close()

out = open('','a')
print(date, file=out)
out.close()