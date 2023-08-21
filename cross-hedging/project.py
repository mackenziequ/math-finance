#### Gather Data ####
# Gold Index: https://finance.yahoo.com/quote/GC%3DF/history/?guccounter=1
# Selected Futures
import pandas as pd
import yfinance as yahooFinance
import matplotlib.pyplot as plt
import numpy as np

data =pd.DataFrame(yahooFinance.download(['GC=F','NEM'], period="5y", interval="3mo")['Close'])
data.to_csv("historical_data.csv")



# Plot
#plt.plot(gold_history)
#plt.plot(gold_mine_stock_price)
#plt.show()



#### Data Analysis ####



#### ####
#### ####
