#import excel files
#Determine

import numpy as np
import pandas as pd

import yfinance as yf
import pandas as pd
import numpy as np

# Fetch historical data
def fetch_data(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    data = stock.history(period="1y") # Fetch data for one year
    return data['Close']

# Calculate daily returns
def calculate_returns(data):
    data_returns = data.pct_change()
    return data_returns.dropna()

# Check price trend
def check_trend(data_returns):
    volatility = np.std(data_returns) # Standard deviation as measure of volatility
    avg_daily_return = np.mean(data_returns)
    
    if avg_daily_return > 0 and volatility < 0.01: # Check your own threshold for volatility
        return "Steady low-volatile climb"
    elif avg_daily_return > 0 and volatility > 0.02: # Check your own threshold for volatility
        return "Frog in the pan"
    else:
        return "No clear trend or pattern"

# Use the functions
data = fetch_data("AAPL")
data_returns = calculate_returns(data)
trend = check_trend(data_returns)

print(trend)
