import yfinance as yf
import numpy as np
np.NaN = np.nan
import pandas_ta as ta
import warnings


# Suppress FutureWarnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Fetch historical data using yfinance
def get_data(ticker, period="5d", interval="1h"):
    data = yf.Ticker(ticker)
    data = data.history(period=period, interval=interval)
    return data

## Calculate the technical indicators
def calculate_indicators(df):
    df['RSI'] = ta.rsi(df['Close'], length=14)
    df['CCI'] = ta.cci(df['High'], df['Low'], df['Close'], length=20)
    df['WILLIAMS'] = ta.willr(df['High'], df['Low'], df['Close'], length=14)
    df['SMI'] = ta.sma(df['Close'], length=14)

    # Calculate MFI and handle large or incompatible values
    mfi_values = ta.mfi(df['High'], df['Low'], df['Close'], df['Volume'], length=14)
    mfi_values = mfi_values.replace([np.inf, -np.inf], np.nan)  # Replace infinities with NaN
    df['MFI'] = mfi_values.astype('float64')  # Ensure MFI column is float64


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
    df['Neutral'] = ~(df['Long'] | df['Short'])
    
    
    return df[['Close', 'RSI', 'CCI', 'WILLIAMS', 'SMI', 'MFI', 'Long', 'Short', 'Neutral']]

# Function to display signals
def display_signals(df):
    # Filter for rows with Long or Short signals
    # signals = df[(df['Long'] == True) | (df['Short'] == True)]
    signals = df
    return signals[['Close', 'RSI', 'CCI', 'WILLIAMS', 'SMI', 'MFI', 'Long', 'Short', 'Neutral']]

def get_last_signal(df):
    last_row = df.iloc[-1]
    return last_row[['Close', 'RSI', 'CCI', 'WILLIAMS', 'SMI', 'MFI', 'Long', 'Short', 'Neutral']]

# Main execution
ticker = 'BTC-USD'  # You can replace this with any ticker symbol
# df = get_data(ticker)
# calculate_indicators(df)
# df = generate_signals(df)
# signals = generate_signals(df)
# # Print the signals where a long or short entry is suggested
# print(signals)





def all(ticker, period="1mo", interval="1h"):
    data = yf.Ticker(ticker)
    data = data.history(period=period, interval=interval)
    df = data
    df['RSI'] = ta.rsi(df['Close'], length=14)
    df['CCI'] = ta.cci(df['High'], df['Low'], df['Close'], length=20)
    df['WILLIAMS'] = ta.willr(df['High'], df['Low'], df['Close'], length=14)
    df['SMI'] = ta.sma(df['Close'], length=14)

    # Calculate MFI and handle large or incompatible values
    mfi_values = ta.mfi(df['High'], df['Low'], df['Close'], df['Volume'], length=14)
    mfi_values = mfi_values.replace([np.inf, -np.inf], np.nan)  # Replace infinities with NaN
    df['MFI'] = mfi_values.astype('float64')  # Ensure MFI column is float64
    
    
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
                  
    # df['Neutral'] = ~(df['Long'] | df['Short'])
    
    # df = df[(df['Long'] == True) | (df['Short'] == True)]
    
    # print(df[['RSI', 'CCI', 'WILLIAMS', 'SMI', 'MFI']].describe())
    
    return df[['Close', 'RSI', 'CCI', 'WILLIAMS', 'SMI', 'MFI', 'Long', 'Short']].iloc[-1]

print(all(ticker))
