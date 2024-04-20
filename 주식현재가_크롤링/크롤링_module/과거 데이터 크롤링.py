from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot plt
import datetime

code = input()

일자 = []
종가 = []
거래량 = []
info_dataframe = []

for i in range (10):
    url = 'htts://finance.naver.com/item/sise_day.nhn?code={}&page={}'.format(code,str(i+1))
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, '')