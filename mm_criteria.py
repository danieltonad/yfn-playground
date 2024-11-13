import yfinance as yf
import pandas as pd

def meets_mm_criteria(ticker):
    # Fetch historical data (1 year + buffer for MAs)
    data = yf.Ticker(ticker).history(period="1y", interval="1d")
    
    if data.empty:
        print(f"No data found for ticker {ticker}")
        return False

    # Calculate Moving Averages
    data['50_MA'] = data['Close'].rolling(window=50).mean()
    data['150_MA'] = data['Close'].rolling(window=150).mean()
    data['200_MA'] = data['Close'].rolling(window=200).mean()

    # Latest available prices and moving averages
    current_close = data['Close'].iloc[-1]
    ma_50 = data['50_MA'].iloc[-1]
    ma_150 = data['150_MA'].iloc[-1]
    ma_200 = data['200_MA'].iloc[-1]
    ma_200_prev = data['200_MA'].iloc[-22]  # MA 22 days ago for trend check
    
    # Calculate 52-week high and low
    high_52wk = data['High'].rolling(window=252).max().iloc[-1]
    low_52wk = data['Low'].rolling(window=252).min().iloc[-1]
    # print(current_close > ma_50 , current_close > ma_150, current_close > ma_200)
    # print(ma_50 > ma_150, ma_50 > ma_200, ma_150 > ma_200, ma_200 > ma_200_prev)
    # print(ma_50, ma_150, ma_200)
    # print((high_52wk - current_close) / high_52wk < 0.25, (current_close - low_52wk) / low_52wk > 0.25)
    
    # Mark Minervini Criteria
    try:
        criteria_met = (
            current_close > ma_50 and  # CMP > 50 MA
            current_close > ma_150 and  # CMP > 150 MA
            current_close > ma_200 and  # CMP > 200 MA
            ma_50 > ma_150 and  # 50 MA > 150 MA
            ma_50 > ma_200 and  # 50 MA > 200 MA
            ma_150 > ma_200 and  # 150 MA > 200 MA
            ma_200 > ma_200_prev and  # 200 MA trending up
            (high_52wk - current_close) / high_52wk < 0.25 and  # Within 25% of 52-week high
            (current_close - low_52wk) / low_52wk > 0.25  # More than 25% above 52-week low
        )
        return criteria_met

    except Exception as e:
        print(f"Error calculating criteria for {ticker}: {e}")
        return False

# 

print(meets_mm_criteria("NVDA"))