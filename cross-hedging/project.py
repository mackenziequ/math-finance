#### Gather Data ####
# Gold Index: https://finance.yahoo.com/quote/GC%3DF/history/?guccounter=1
# Selected Futures
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression

data =pd.DataFrame(yf.download(['GC=F','NEM'], period="5y", interval="1mo")['Close']).iloc[::3, :].dropna()
data.to_csv("cross-hedging/historical_data.csv")

# Plot
# plt.plot(data)
# plt.plot(gold_mine_stock_price)
# plt.show()



#### Data Analysis ####
def get_change_in_price(arr):
    change = []
    for i in range(len(arr)-1):
        change.append(arr[i+1]-arr[i])
    return np.array(change)

gold_price = data["GC=F"].to_numpy()
delta_f = get_change_in_price(gold_price)
gold_mine_price = data["NEM"].to_numpy()
delta_s = get_change_in_price(gold_mine_price)
print(delta_f, delta_s)



# Regression
reg = LinearRegression().fit(delta_f.reshape(-1, 1), delta_s.reshape(-1, 1))
plt.scatter(delta_f,delta_s)
plt.plot(delta_f, reg.predict(delta_f.reshape(-1, 1)), color = "green")
plt.savefig("cross-hedging/regression.jpeg")

# Hedge effectiveness
def rho(del_s, del_f):
    # returns correlation
    rho = np.corrcoef(del_s, del_f)
    return rho[0][1]

## Note: Fix hedge effectiveness
print(rho(delta_s, delta_f), rho(delta_s, delta_f)**2, sklearn.metrics.r2_score(delta_f, reg.predict(delta_f.reshape(-1, 1))))

#### ####
#### ####
