import yfinance as yf
import pandas as pd
import datetime

# Define a list of stock symbols to check
symbols = ['AAPL', 'MSFT', 'GOOGL']  # Replace with desired symbols

# Define date range for moving averages
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=365)

# Function to check if a stock meets Minervini's criteria
def check_minervini_criteria(stock_data):
    # Calculate moving averages
    stock_data['50 MA'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['150 MA'] = stock_data['Close'].rolling(window=150).mean()
    stock_data['200 MA'] = stock_data['Close'].rolling(window=200).mean()
    
    # Latest values
    cmp = stock_data['Close'].iloc[-1]
    ma_50 = stock_data['50 MA'].iloc[-1]
    ma_150 = stock_data['150 MA'].iloc[-1]
    ma_200 = stock_data['200 MA'].iloc[-1]
    ma_200_prev = stock_data['200 MA'].iloc[-2]  # Check if 200 MA is trending up
    
    # 52-week high and low
    high_52week = stock_data['Close'].max()
    low_52week = stock_data['Close'].min()
    
    # Criteria checks
    criteria = {
        "CMP > 50MA": cmp > ma_50,
        "CMP > 150MA": cmp > ma_150,
        "CMP > 200MA": cmp > ma_200,
        "50MA > 150MA": ma_50 > ma_150,
        "50MA > 200MA": ma_50 > ma_200,
        "150MA > 200MA": ma_150 > ma_200,
        "200MA trending up": ma_200 > ma_200_prev,
        "Within 25% of 52-week High": cmp >= 0.75 * high_52week,
        ">25% up from 52-week Low": cmp >= 1.25 * low_52week,
    }
    
    return all(criteria.values()), criteria  # Return if all criteria met and individual results

# Main loop to check each stock
results = {}
for symbol in symbols:
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    meets_criteria, details = check_minervini_criteria(stock_data)
    results[symbol] = {"Meets Criteria": meets_criteria, **details}

# Display results
results_df = pd.DataFrame(results).T
print(results_df)