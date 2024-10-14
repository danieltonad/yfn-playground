import yfinance as yf

# Define the stock ticker
ticker = 'SATS-USD'

# Get the stock data
stock = yf.Ticker(ticker)

# Fetch the income statement data
# income_stmt = stock.quarterly_financials

# # Extract EPS data from the income statement
# eps_basic = income_stmt.loc['Basic EPS']
# eps_diluted = income_stmt.loc['Diluted EPS']
# sales = income_stmt.loc['Total Revenue']

# print(eps_basic, eps_diluted)

def check_eps_increase_status(eps_data, threshold=0.20):
    growth_status = []

    for i in range(1, len(eps_data)):
        current_eps = eps_data.iloc[i]
        previous_eps = eps_data.iloc[i-1]
        print(previous_eps, current_eps)
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


stock.history()
