import yfinance as yf
import pandas as pd

# Define the stock ticker
ticker = 'BTC-USD'

# Get the stock data
stock = yf.Ticker(ticker)

# Fetch the income statement data
# income_stmt = stock.quarterly_financials

# # Extract EPS data from the income statement
# eps_basic = income_stmt.loc['Basic EPS']
# eps_diluted = income_stmt.loc['Diluted EPS']
# sales = income_stmt.loc['Total Revenue']

# print(eps_basic, eps_diluted)

def calculate_percentage_increase(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    data = ticker.history(period="ytd")
    
    if not data.empty:
        first_close = data['Close'].iloc[0]  # First closing price
        last_close = data['Close'].iloc[-1]  # Last closing price
        print(last_close, first_close)
        percentage_increase = ((last_close - first_close) / first_close) * 100
        return round(percentage_increase, 2)
    else:
        return "No data available for the ticker."
    
def calculate_yearly_percentage_increase(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    data = ticker.history(period="max")
    
    if not data.empty:
        # Resample data to get the last trading day of each year using 'A' for annual frequency
        yearly_data = data['Close'].resample('YE').last()
        # Calculate the yearly percentage change
        yearly_percentage_increase = yearly_data.pct_change() * 100
        
        avg_yearly_increase = yearly_percentage_increase.mean()
        
        return avg_yearly_increase
    else:
        return "No data available for the ticker."
    
def calculate_n_year_change(ticker_symbol, n_years):
    ticker = yf.Ticker(ticker_symbol)
    data = ticker.history(period="max")
    
    if not data.empty:
        # Resample to get closing prices every n years (custom interval)
        n_year_data = data['Close'].resample(f'{n_years}Y').last()
        
        # Calculate the n-year percentage changes
        n_year_percentage_change = n_year_data.pct_change().dropna() * 100
        
        return n_year_percentage_change
    
    else:
        return None


def check_eps_increase_status(eps_data, threshold=0.20):
    growth_status = []

    for i in range(1, len(eps_data)):
        current_eps = eps_data.iloc[i]
        previous_eps = eps_data.iloc[i-1]
        growth_rate = (previous_eps - current_eps) / current_eps
        growth_status.append(growth_rate > threshold and previous_eps > 0 and current_eps > 0)
        # print(current_eps)
    print(growth_status)
    growth_status = growth_status[:4]
    return all(growth_status)

# eps_basic_status = check_eps_increase_status(eps_basic)
# eps_diluted_status = check_eps_increase_status(eps_diluted)
# sales_status = check_eps_increase_status(sales)
# print(eps_basic_status, eps_diluted_status)


# SALES Q/Q
#


# print(stock.history(period="max", interval="1wk"))

# print(calculate_n_year_change("BTC-USD", 3))
print(calculate_percentage_increase("BTC-USD"))
