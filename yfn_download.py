import yfinance as yf
import pandas as pd

def save_to_csv(data, filename):
    filename = "./data/" + filename
    if not data.empty:
        data.to_csv(filename)
        print(f"Saved {filename}")
    else:
        print(f"No data available to save for {filename}")

def save_to_text(data, filename):
    with open(filename, "w") as file:
        file.write(str(data))
    print(f"Saved {filename}")

def get_ticker_info(ticker_symbol):
    # Fetch the ticker data
    ticker = yf.Ticker(ticker_symbol)
    
    # Download historical data for the ticker
    print("Downloading historical market data...")
    historical_data = ticker.history(period="max")
    save_to_csv(historical_data, f"{ticker_symbol}_historical_data.csv")

    # Save General Info
    print("Fetching information for:", ticker_symbol)
    info = ticker.info
    save_to_text(info, f"{ticker_symbol}_info.txt")

    # Stock Actions (Splits, Dividends)
    stock_actions = ticker.actions
    save_to_csv(stock_actions, f"{ticker_symbol}_actions.csv")

    # Dividends
    dividends = ticker.dividends
    save_to_csv(dividends, f"{ticker_symbol}_dividends.csv")

    # Stock Splits
    splits = ticker.splits
    save_to_csv(splits, f"{ticker_symbol}_splits.csv")

    # Financials (Income Statement)
    financials = ticker.financials
    save_to_csv(financials, f"{ticker_symbol}_financials.csv")

    # Balance Sheet
    balance_sheet = ticker.balance_sheet
    save_to_csv(balance_sheet, f"{ticker_symbol}_balance_sheet.csv")

    # Cashflow Statement
    cashflow = ticker.cashflow
    save_to_csv(cashflow, f"{ticker_symbol}_cashflow.csv")

    # Earnings
    earnings = ticker.earnings
    save_to_csv(earnings, f"{ticker_symbol}_earnings.csv")

    # Sustainability (ESG Scores)
    sustainability = ticker.sustainability
    save_to_csv(sustainability, f"{ticker_symbol}_sustainability.csv")

    # Analysts Recommendations
    recommendations = ticker.recommendations
    save_to_csv(recommendations, f"{ticker_symbol}_recommendations.csv")

    # Institutional Holders
    institutional_holders = ticker.institutional_holders
    save_to_csv(institutional_holders, f"{ticker_symbol}_institutional_holders.csv")

    # Major Holders
    major_holders = ticker.major_holders
    save_to_csv(major_holders, f"{ticker_symbol}_major_holders.csv")

if __name__ == "__main__":
    # Example: Get information about Apple (AAPL)
    ticker_symbol = input("Enter the ticker symbol (e.g., AAPL, TSLA): ").upper()
    get_ticker_info(ticker_symbol)
