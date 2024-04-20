import matplotlib.pyplot as plt
import numpy as np

#파일불러오기
testfile = open('date','r')
day = testfile.readlines() #리스트로 읽음
# print('day:', day)

testfile = open('AAPL+EDV','r')
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