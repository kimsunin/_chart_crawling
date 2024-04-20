import requests
from bs4 import BeautifulSoup

# 삼성
url = "https://finance.naver.com/item/sise.naver?code=005930"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
price = soup.select_one("#_nowVal").text
print("삼성전자:", price)

#데이터저장
out = open('output.txt','w')
print(price, file=out)

