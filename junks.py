import yfinance as yf

# Fetch weekly data using yfinance's history method and check for high and low crossovers
def check_high_low_cross(ticker, period="1y"):
    # Fetch weekly data
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval="1d")
    weekly_df = df.resample('W').agg({'High': 'max', 'Low': 'min'})

    # Ensure there are at least two weeks of data
    if len(weekly_df) < 2:
        return (False, False)

    # Get current and previous week's high and low
    current_week_high = weekly_df['High'].iloc[-1]
    prev_week_high = weekly_df['High'].iloc[-2]
    current_week_low = weekly_df['Low'].iloc[-1]
    prev_week_low = weekly_df['Low'].iloc[-2]

    # Check if new high is greater and if new low is lower
    high_crossover = current_week_high > prev_week_high
    low_crossover = current_week_low < prev_week_low

    # Return tuple (high_crossover, low_crossover)
    return (high_crossover, low_crossover)

# Main execution
ticker = 'AAPL'  # Replace with your desired ticker

# Check for both high and low crossovers
high_crossover, low_crossover = check_high_low_cross(ticker)

print(f"High crossover: {high_crossover}, Low crossover: {low_crossover}")
