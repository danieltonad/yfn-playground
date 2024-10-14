import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import time

def get_earnings_data(ticker, years=3):
    stock = yf.Ticker(ticker)

    # Get the quarterly financials
    financials = stock.quarterly_financials

    if financials.empty:
        return None

    # Filter for earnings (net income)
    earnings = financials.loc['Net Income']

    # Sort by index in descending order and get the last 'years' years of data
    earnings = earnings.sort_index(ascending=False)
    earnings = earnings.head(years * 4)  # Get last 'years' years of quarterly data

    return earnings

def calculate_growth_rates(earnings):
    # Calculate YoY growth rates
    growth_rates = earnings.pct_change(-1)
    return growth_rates.dropna()

def check_earnings_acceleration(ticker):
    earnings = get_earnings_data(ticker)
    if earnings is None:
        return False
    
    growth_rates = calculate_growth_rates(earnings)
    
    if len(growth_rates) < 4:
        return False
    
    # Check for positive growth rate
    if not all(growth_rates > 0):
        return False
    
    # Check for increasing growth rate
    if not all(growth_rates.diff() > 0):
        return False
    
    # Check for consistency over several quarters
    if not all(growth_rates.rolling(window=4).mean().diff() > 0):
        return False
    
    # Additional checks can be added here for industry comparison and revenue growth alignment
    
    return True

def get_sp500_tickers():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    table = pd.read_html(url)[0]
    return table['Symbol'].tolist()

def update_watchlist():
    tickers = get_sp500_tickers()
    watchlist = []
    
    for ticker in tickers:
        print(f"Analyzing {ticker}...")
        if check_earnings_acceleration(ticker):
            watchlist.append(ticker)
        time.sleep(1)  # To avoid hitting API rate limits
    
    return watchlist

def main():
    while True:
        print("Updating watchlist...")
        watchlist = update_watchlist()
        
        print("\nCurrent Earnings Acceleration Watchlist:")
        for ticker in watchlist:
            print(ticker)
        
        print("\nWaiting for next update...")
        time.sleep(7 * 24 * 60 * 60)  # Wait for a week

if __name__ == "__main__":
    main()