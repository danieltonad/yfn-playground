import yfinance as yf

# Fetch stock data
ticker = yf.Ticker("AAPL")  # Replace 'AAPL' with your desired stock symbol

# Fetch average volume (from the 'info' attribute)
print(ticker.info)
avg_volume = ticker.info['averageVolume']
print(f"Average Volume: {avg_volume}")
