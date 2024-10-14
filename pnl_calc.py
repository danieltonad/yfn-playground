import yfinance as yf
import pandas as pd
import json, csv
import numpy as np
import datetime

today = datetime.datetime.today()


def save_json(data: list, name: str):
    with open(f'{name}.json', 'w') as file:
        # Step 4: Use json.dump() to write the list to the file
        json.dump(data, file, indent=4)
        

def extract_values_from_file(file_path):
    # Initialize an empty list to store the extracted values
    values = []

    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace and split the line by the colon
            parts = line.strip().split(':')
            # if parts[-2] == "COINBASE":
            values.append(parts[-1])

    return values

def sort_json_file(file_path, key="total_pnl"):
    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Ensure the data is a list
    if not isinstance(data, list):
        raise ValueError("The JSON data must be a list of objects.")

    # Sort the data based on the specified key in descending order
    sorted_data = sorted(data, key=lambda x: x.get(key, 0), reverse=True)

    # Optionally, write the sorted data back to a file
    with open(file_path, 'w') as file:
        json.dump(sorted_data, file, indent=4)

    return sorted_data

def read_csv_to_tuple_array(csv_file):
    try:
        # Initialize an empty list to store the tuples
        result = []
        
        # Open and read the CSV file
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 2 or row[0] == "Ticker":
                    continue  # Skip rows that don't have exactly 2 columns
                ticker = row[0].strip()
                date_str = row[1].strip()
                result.append((ticker, date_str))
        
        return result
    
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return []

def json_to_csv(json_file_path, csv_file_path):
    # Read the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Ensure the data is a list of dictionaries
    # if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
    #     raise ValueError("The JSON data must be a list of dictionaries.")

    # Extract the keys for the CSV header
    if data:
        keys = data[0].keys()
    else:
        keys = []

    # Write the data to a CSV file
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)

        # Write the header
        writer.writeheader()

        # Write the rows
        for item in data:
            writer.writerow(item)
      
def crypto_format(crypto_asset: str) -> str:
        if crypto_asset.endswith("USD"):
            return f"{crypto_asset[:-3]}-{crypto_asset[-3:]}"
        return crypto_asset      

def calculate_mean_x_total_pnl(ticker, investment_amount=100, years=5):
    try:
        # Get the stock data
        stock = yf.Ticker(ticker)
        end_date = pd.to_datetime('today')
        start_date = end_date - pd.DateOffset(years=years)
        hist = stock.history(start=start_date, end=end_date)

        if 'Open' not in hist.columns:
            raise ValueError("Historical data does not include 'Open' prices.")

        # Initialize variables
        total_qty_bought = 0
        total_amount_spent = 0
        total_pnl = 0
        current_qty_bought = 0
        current_amount_spent = 0
        mean_price = 0

        # Fetch the current opening price
        current_open_price = stock.history(period="1d")['Open'].iloc[0]

        # Iterate through each day
        for index, row in hist.iterrows():
            open_price = float(row['Open'])
            shares_bought = investment_amount / open_price

            # Update current quantities and amounts
            current_qty_bought += shares_bought
            current_amount_spent += investment_amount
            mean_price = current_amount_spent / current_qty_bought
            print(mean_price)
            # Check if the current opening price is 2X the mean price
            if open_price >= 2 * mean_price:
                # Take profit
                profit = current_qty_bought * open_price - current_amount_spent
                total_pnl += profit

                # Update total quantities and amounts
                total_qty_bought += current_qty_bought
                total_amount_spent += current_amount_spent

                # Reset current quantities and amounts
                current_qty_bought = 0
                current_amount_spent = 0
                mean_price = 0
            # else:
            #     # Update total quantities and amounts
            #     total_qty_bought += current_qty_bought
            #     total_amount_spent += current_amount_spent

        # Calculate the total value of the investment at the current opening price
        total_value = total_qty_bought * current_open_price
        total_pnl += total_value - total_amount_spent

        return total_amount_spent, total_value, total_pnl, total_qty_bought

    except Exception as err:
        print(err)
        return False, False, False, False

def calculate_total_pnl(ticker, investment_amount=100, years=5):
    try:
        # Get the stock data
        stock = yf.Ticker(ticker)
        end_date = pd.to_datetime('today')
        start_date = end_date - pd.DateOffset(years=years)
        hist = stock.history(start=start_date, end=end_date)
        if 'Open' not in hist.columns:
            raise ValueError("Historical data does not include 'Open' prices.")
        # Calculate the number of shares bought each day
        hist['Shares Bought'] = investment_amount / hist['Open']
        # Calculate the total investment
        total_investment = investment_amount * len(hist)
        # Fetch the current opening price
        current_open_price = stock.history(period="1d")['Open'].iloc[0]
        # Calculate the total value of the investment at the current opening price
        inf_mask = hist['Shares Bought'].isin([np.inf, -np.inf])
        hist = hist[~inf_mask]
        total_shares_bought = hist['Shares Bought'].sum()
        total_value = total_shares_bought * current_open_price
        # Calculate the total PnL
        total_pnl = total_value - total_investment
        return total_investment, total_value, total_pnl, total_shares_bought
    
    except Exception as err:
        print(err)
        return False, False, False, False


def calculate_total_pnl_custom_date(ticker, start_date, end_date, investment_amount=100):
    try:
        # Parse the custom start and end dates in "mm/dd/yyyy" format
        start_date = pd.to_datetime(start_date, format="%m/%d/%Y")
        end_date = pd.to_datetime(end_date, format="%m/%d/%Y")

        # Get the stock data
        stock = yf.Ticker(ticker)

        # Fetch historical price data for the given date range
        hist = stock.history(start=start_date, end=end_date)

        # Ensure the data includes the 'Open' price
        if 'Open' not in hist.columns:
            raise ValueError("Historical data does not include 'Open' prices.")

        # Calculate the number of shares bought each day
        hist['Shares Bought'] = investment_amount / hist['Open']

        # Calculate the total investment
        total_investment = investment_amount * len(hist)

        # Fetch the most recent opening price (assumes the most recent is the end date)
        current_open_price = stock.history(period="1d")['Open'].iloc[0]

        # Remove any rows with infinite values in 'Shares Bought'
        inf_mask = hist['Shares Bought'].isin([np.inf, -np.inf])
        hist = hist[~inf_mask]

        # Calculate the total shares bought
        total_shares_bought = hist['Shares Bought'].sum()

        # Calculate the total value of the investment at the current opening price
        total_value = total_shares_bought * current_open_price

        # Calculate the total PnL
        total_pnl = total_value - total_investment

        return total_investment, total_value, total_pnl, total_shares_bought
    
    except Exception as err:
        print(f"Error: {err}")
        return False, False, False, False

def print_report(tickers, years=5, amount=100):
    global all, count
    for ticker in tickers:
        ticker = ticker.replace("/", "-")
        # ticker = crypto_format(ticker)
        count +=1
        total_investment, total_value, total_pnl, qty = calculate_total_pnl(ticker, investment_amount=amount, years=years)
        if total_investment and total_value and total_pnl and qty:
            obj = {"ticker": ticker, "total_investment": total_investment, "quantity": qty ,"total_value": total_value, "total_pnl": total_pnl}
            all.append(obj)
        print(f"Progress: {count:,} of {total}", end="\r")
        # print(ticker)
        # print(f"Total Investment: ${total_investment:,.2f}")
        # print(f"Total Qty: {qty:,.2f}")
        # print(f"Total Value: ${total_value:,.2f}")
        # print(f"Total PnL: ${total_pnl:,.2f}\n\n")

def print_mean_report(tickers):
    global all, count
    for ticker in tickers:
        ticker = ticker.replace("/", "-")
        # ticker = crypto_format(ticker)
        count +=1
        total_investment, total_value, total_pnl, qty = calculate_mean_x_total_pnl(ticker, investment_amount=100, years=5)
        if total_investment and total_value and total_pnl and qty:
            obj = {"ticker": ticker, "total_investment": total_investment, "quantity": qty ,"total_value": total_value, "total_pnl": total_pnl}
            all.append(obj)
        print(f"Progress: {count:,} of {total}", end="\r")
        
        # print(ticker)
        # print(f"Total Investment: ${total_investment:,.2f}")
        # print(f"Total Qty: {qty:,.2f}")
        # print(f"Total Value: ${total_value:,.2f}")
        # print(f"Total PnL: ${total_pnl:,.2f}\n\n")

def print_report_custom_date(tickers):
    global all, count
    current_date_str = today.strftime("%m/%d/%Y")
    for ticker, date_str in tickers:
        ticker = ticker.replace("/", "-")
        # ticker = crypto_format(ticker)
        count +=1
        total_investment, total_value, total_pnl, qty = calculate_total_pnl_custom_date(ticker, start_date=date_str, end_date=current_date_str ,investment_amount=100)
        if total_investment and total_value and total_pnl and qty:
            obj = {"ticker": ticker, "total_investment": total_investment, "quantity": qty ,"total_value": total_value, "total_pnl": total_pnl}
            all.append(obj)
        print(f"Progress: {count:,} of {total}", end="\r")
        # print(f"Total Investment: ${total_investment:,.2f}")
        # print(f"Total Qty: {qty:,.2f}")
        # print(f"Total Value: ${total_value:,.2f}")
        # print(f"Total PnL: ${total_pnl:,.2f}\n\n")

all = []
count, total = 0,0
# stocks = extract_values_from_file("C:\\Users\\SOLARIN\\Desktop\\Syarpa\\tradingview_watchlist\\temp\\stocks.txt")
# stocks = read_csv_to_tuple_array("finviz_sample.csv")
stocks = [
    "VTWO.MX", "VCR.MX", "VT.MX", "VDE", "VTIP.MX", "VWO.MX", "VNQ", "VPU", "VCR", "VWO",
    "VAW", "IVOG", "VTV.MX", "VNQI", "VYMI", "VOE", "VPL", "VEA.MX", "VIGI", "VIS", "IVOO",
    "BND.MX", "VNQ.MX", "VOT", "VO", "VXUS", "VOOV", "VSS", "VEU", "VDC", "VYM", "VEA",
    "VTV", "VONV", "IVOV", "VIG", "VSGX", "MGV", "VT", "VTHR", "VGK", "VV", "VBR", "VONE",
    "VB", "VUG", "VTI", "VOO", "VFQY", "VFMV", "VGK.MX", "VBK", "VFMF", "VONG", "MGC",
    "MGK", "VIOG", "ESGV", "VFH", "VOOG", "VOO.MX", "BNDX", "VTES", "VFVA", "VOX", "VXF",
    "VIOO", "VTEC", "VUSB", "VGSH", "BNDX.MX", "VGSH.MX", "VFH.MX", "VEU.MX", "VOX.MX",
    "VTI.MX", "VXUS.MX", "VDC.MX", "VYM.MX", "VPL.MX", "EDV.MX", "VUG.MX", "VDE.MX",
    "VGT.MX", "VHT.MX", "VIS.MX", "VBR.MX", "BNDW", "VTEI", "VTIP", "VGT", "BSV", "VGIT",
    "VTEB", "VMBS", "BND", "VCSH", "VCEB", "VCRB", "VPLS", "VCIT", "VIOV", "VFMO", "BIV",
    "VTC", "VGLT", "VWOB", "BLV", "VCLT", "EDV", "VHT", "VTWV", "VTWG", "VTWO"
]

total = len(stocks)
# print(total, stocks)

# print_mean_report(["AAPL"])
print_report(stocks)



# Save JSON
save_json(all, "vanguard")


# sort stocks
sorted = sort_json_file("vanguard.json")
save_json(sorted, "vanguard")
print("Done")




json_to_csv("vanguard.json", "vanguard.csv")




