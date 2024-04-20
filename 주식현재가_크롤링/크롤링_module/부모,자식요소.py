import requests
from bs4 import BeautifulSoup


#부모,자식요소
url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
price = soup.select_one("#Col1-1-HistoricalDataTable-Proxy > section:first-child > div:nth-child(2) > table:first-child > tbody:first-child")
# print(price.get_attribute_list("value"))
# print(price.get_attribute)
# prices = str(price.get_attribute_list("value"))

# a = '.Fw'+chr(40)+'b'+chr(41)
print(price)