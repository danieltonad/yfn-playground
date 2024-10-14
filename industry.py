import yfinance as yf

def get_asset_info(ticker_symbol):
    try:
        # Create a Ticker object for the specified asset
        ticker = yf.Ticker(ticker_symbol)

        # Fetch the asset's info
        asset_info = ticker.info

        # Extract the sector and industry information
        sector = asset_info.get('sector', 'N/A')
        industry = asset_info.get('industry', 'N/A')
        
        data = ticker.history(period="1y")

        return sector, industry, data
    except Exception as err:
        print("Error:", str(err))

# Example usage
ticker_symbol = 'ES=F'  #Replace with the desired ticker symbol
sector, industry, data = get_asset_info(ticker_symbol)

print(f"Sector: {sector}")
print(f"Industry: {industry}")

print(data)
