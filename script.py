import yfinance as yf


def get_highest_weekly_volume_ever(self, asset) -> tuple:
    try:
        ticker = asset.split(":")[-1]
        ticker = ticker.replace("/", "-")
        ticker = yf.Ticker(ticker)
        
        data = ticker.history(period="max", interval="1wk")
        # [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
        
        # Adding a shift to get the previous week's close
        data['Prev_Close'] = data['Close'].shift(1)
        
        # Determine if volume is positive or negative
        data['Volume_Trend'] = data.apply(lambda row: '+' if row['Close'] > row['Prev_Close'] else '-', axis=1)
        
        highest_volume = data['Volume'].max()
        highest_volume_date = data['Volume'].idxmax().to_pydatetime().strftime("%d-%m-%Y %H:%M:%S")
        
        # Get whether the volume on the highest volume day was positive or negative
        volume_trend = data.loc[data['Volume'].idxmax(), 'Volume_Trend']
        
        return highest_volume.item(), highest_volume_date, volume_trend
    
    except Exception as err:
        return False, None, None


def check_stock_trend(asset, interval, period) -> str:
    try:
        ticker = asset.split(":")[-1]
        ticker = ticker.replace("/", "-")
        ticker = yf.Ticker(ticker)
        
        data = ticker.history(period=period, interval=interval)
        # Fetch data for the past two days
        prev_close = data['Close'].iloc[0]  # Previous day close
        curr_close = data['Close'].iloc[1]  # Current day close

        # Determine if stock is bullish or bearish based on closing price
        if curr_close > prev_close:
            return "+"
        else:
            return "-"
    
    except Exception as err:
        return str(err)

# Example usage:
result = check_stock_trend("ELF", interval="5d", period="max")
print(result)  # Output will be '+' for bullish, '-' for bearish

    
    

# print(get_highest_weekly_volume_ever("", "ELF"))
