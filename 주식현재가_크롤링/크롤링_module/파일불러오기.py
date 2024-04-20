#파일불러오기
testfile = open('date','r')
day = testfile.readlines() #리스트로 읽음
# print('day:', day)

testfile = open('AAPL+EDV','r')
price = testfile.readlines() #리스트로 읽음