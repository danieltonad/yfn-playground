import yfinance as yf

# ticker = yf.Ticker('AAPL').history(period="max")

# ticker.to_csv("aapl-history-max.csv", columns=["Close"])

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

print(get_earnings_data("AAPL"))