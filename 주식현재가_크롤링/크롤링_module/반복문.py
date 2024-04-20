import requests
from bs4 import BeautifulSoup

total = 0
answer = 'YES'

while answer == 'YES' :
    name = input('종목:')
    
    url = 'https://finance.yahoo.com/quote/'+name+'?p='+name+'&.tsrc=fin-srch'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one(".Fw\(b\).Fz\(36px\).Mb\(-4px\).D\(ib\)").text
    price = float(price)
    print(name+':', price)
    
    total += price
    answer = input('계속?(YES/NO): ')
print('total:', total)


# total = 0
# answer = '반복'

# while answer == '반복':
#     x = int(input('숫자입력:'))
#     total += x
#     answer = input('반복/정지:')
# print('합:', total)