import requests
from bs4 import BeautifulSoup as bs

import requests

def get_realtime_stock_price_alpha_vantage(symbol: str, api_key: str) -> float:
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": api_key
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if "Global Quote" in data and "05. price" in data["Global Quote"]:
            return float(data["Global Quote"]["05. price"])
        else:
            print(f"Error: {data.get('Note', 'No valid data received.')}")
            return None
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None





def stock_details(exchange: str, ticker: str):
    response = requests.get(f"https://www.tradingview.com/symbols/{exchange.upper()}-{ticker.upper()}/")
    raw_html = response.text
    html = bs(raw_html, "html.parser")
    divs = html.find_all("div")
    print(divs[1211].text)
    

stock_details(exchange="NYSE", ticker="KVYO")
    