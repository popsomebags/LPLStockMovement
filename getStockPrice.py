import yfinance as yf
import matplotlib.pyplot as plt

ticker = "LPLA"

quarter = input("Enter the quarter you would like to see (Q1, Q2, Q3, Q4): ")
if quarter == "Q1":
    start_date = "2022-01-01"
    end_date = "2022-03-31"

stock_data = yf.download(ticker, start=start_date, end=end_date)

plt.plot(stock_data["Close"])
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title(f"{ticker} Stock Price")

plt.show()