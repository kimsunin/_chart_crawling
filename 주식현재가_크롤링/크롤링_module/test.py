import yfinance as yf

# 종목명 입력받기
symbol = input("주식 종목명을 입력하세요: ")

# yfinance.Ticker() 함수를 사용하여 해당 종목의 데이터 가져오기
ticker = yf.Ticker(symbol)

# 데이터 가져오기
data = ticker.history(period="1d")

# 데이터 출력
print(data)