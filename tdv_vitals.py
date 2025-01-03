import requests
from bs4 import BeautifulSoup as bs



def stock_details(exchange: str, ticker: str):
    response = requests.get(f"https://www.tradingview.com/symbols/{exchange.upper()}-{ticker.upper}/")
    raw_html = response.text
    bs.
    print(raw_html)
    
    
stock_details(exchange="nsdaq", ticker="tsla")
    