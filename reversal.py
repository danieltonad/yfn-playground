import pandas as pd
import yfinance as yf
import pandas_ta as ta
import numpy as np

# Fetch historical data using yfinance
def get_data(ticker, period="1y", interval="1d"):
    data = yf.download(ticker, period=period, interval=interval)
    return data

# Calculate the technical indicators
def calculate_indicators(df):
    df['RSI'] = ta.rsi(df['Close'], length=14)
    df['CCI'] = ta.cci(df['High'], df['Low'], df['Close'], length=20)
    df['WILLIAMS'] = ta.willr(df['High'], df['Low'], df['Close'], length=14)
    df['SMI'] = ta.sma(df['Close'], length=14)
    df['MFI'] = ta.mfi(df['High'], df['Low'], df['Close'], df['Volume'], length=14)
    
    # Handle NaN values after calculating indicators
    df.fillna(method='bfill', inplace=True)  # Backfill to handle initial NaNs
    df.fillna(0, inplace=True)  # Or use 0 for remaining NaNs if preferred

# Define the overbought and oversold conditions and generate signals
def generate_signals(df):
    # Overbought/oversold levels
    rsiOverbought = 70
    rsiOversold = 30
    cciOverbought = 100
    cciOversold = -100
    williamsOverbought = -20
    williamsOversold = -80
    smiOverbought = 40
    smiOversold = -40
    mfiOverbought = 80
    mfiOversold = 20

    # Long (Buy) signal when all are oversold
    df['Long'] = (df['RSI'] < rsiOversold) & (df['CCI'] < cciOversold) & \
                 (df['WILLIAMS'] < williamsOversold) & (df['SMI'] < smiOversold) & \
                 (df['MFI'] < mfiOversold)

    # Short (Sell) signal when all are overbought
    df['Short'] = (df['RSI'] > rsiOverbought) & (df['CCI'] > cciOverbought) & \
                  (df['WILLIAMS'] > williamsOverbought) & (df['SMI'] > smiOverbought) & \
                  (df['MFI'] > mfiOverbought)

    return df

# Function to display signals
def display_signals(df):
    # Filter for rows with Long or Short signals
    signals = df[(df['Long'] == True) | (df['Short'] == True)]
    return signals[['Close', 'RSI', 'CCI', 'WILLIAMS', 'SMI', 'MFI', 'Long', 'Short']]

# Main execution
ticker = 'AAPL'  # You can replace this with any ticker symbol
df = get_data(ticker)
calculate_indicators(df)
df = generate_signals(df)
signals = display_signals(df)

# Print the signals where a long or short entry is suggested
print(signals)
