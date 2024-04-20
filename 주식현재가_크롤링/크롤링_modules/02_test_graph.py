import matplotlib.pyplot as plt
import numpy as np

#날짜
testFile1 = open('날짜','r')  # 'r' read의 약자, 'rb' read binary 약자 (그림같은 이미지 파일 읽을때)
day = testFile1.readlines()
print("날짜:", day) #day = ?/?

#날짜파일 주가파일 따로저장->두 값을 불러와서 그래프 x,y로 표현

#주가
testFile2 = open('삼성+sk','r')  # 'r' read의 약자, 'rb' read binary 약자 (그림같은 이미지 파일 읽을때)
price = testFile2.readlines()
print("삼성+sk:", price)

prices = list(map(int, price))

# days = []
# prices = []
# if day not in days:
#     days.append(day)
#     prices.append(price) #왜 if문을 쓰지?

# prices = list(map(int, prices))

# #그래프
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