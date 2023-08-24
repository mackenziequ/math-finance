#### Gather Data ####
# Gold Index: https://finance.yahoo.com/quote/GC%3DF/history/?guccounter=1
# Selected Futures
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

data =pd.DataFrame(yf.download(['GC=F','NEM'], period="5y", interval="1mo")['Close']).iloc[::3, :].dropna()
data.to_csv("cross-hedging/historical_data.csv")

# Plot
#plt.plot(data)
#plt.plot(gold_mine_stock_price)
#plt.show()



#### Data Analysis ####
def get_change_in_price(arr):
    change = []
    for i in range(len(arr)-1):
        change.append(arr[i+1]-arr[i])
    return change

gold_price = data["GC=F"].to_numpy()
delta_f = get_change_in_price(gold_price)
gold_mine_price = data["NEM"].to_numpy()
delta_s = get_change_in_price(gold_mine_price)

plt.scatter(delta_f,delta_s)
plt.show()
plt.savefig("cross-hedging/scatterplot.png")
#### ####
#### ####
