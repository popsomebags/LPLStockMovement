from tkinter import *
import yfinance as yf
import matplotlib.pyplot as plt

root = Tk()
root.title('2022 Stock Chart')

tick = Entry(root, width=50)
tick.pack()
tick.insert(0, "Enter the ticker name")

def getStock():
    ticker = tick.get()
    stock_data = yf.download(ticker, start="2022-01-01", end="2022-12-31")

    plt.plot(stock_data["Close"])
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.title(f"{ticker} Stock Price")

    plt.show()

myButton = Button(root, text="Generate Plot", command=getStock)
myButton.pack()

root.mainloop()
