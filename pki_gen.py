import yfinance as yf
import pandas as pd
import pickle
import pandas_ta as ta

# Download historical data for Tesla
tsla = yf.Ticker("TSLA")
hist = tsla.history(period="max")

# Calculate technical indicators
hist['MA50'] = ta.sma(hist['Close'], length=50)
hist['MA200'] = ta.sma(hist['Close'], length=200)
hist['RSI'] = ta.rsi(hist['Close'], length=14)
macd = ta.macd(hist['Close'], fast=12, slow=26, signal=9)
hist['MACD'] = macd['MACD_12_26_9']
hist['MACD_Signal'] = macd['MACDs_12_26_9']
hist['MACD_Hist'] = macd['MACDh_12_26_9']

# Save to pickle file
with open('model_input/tsla.pkl', 'wb') as file:
    pickle.dump(hist, file)
