import os, pandas as pd, io
from dotenv import load_dotenv
from enum import Enum

class FINVIZ_ANALYSIS(Enum):
    STRONG_BUY = "STRONG_BUY"
    BUY_BETTER = "BUY_BETTER"
    BUY = "BUY"
    HOLD_BETTER = "HOLD_BETTER"
    HOLD = "HOLD"
    HOLD_WORSE = "HOLD_WORSE"
    SELL = "SELL"
    SELL_WORSE = "SELL_WORSE"
    STRONG_SELL = "STRONG_SELL"
    
    @staticmethod
    def filter(analysis: 'FINVIZ_ANALYSIS') -> str:
        filters = {
            FINVIZ_ANALYSIS.STRONG_BUY: "strongbuy",
            FINVIZ_ANALYSIS.BUY_BETTER: "buybetter",
            FINVIZ_ANALYSIS.BUY: "buy",
            FINVIZ_ANALYSIS.HOLD_BETTER: "holdbetter",
            FINVIZ_ANALYSIS.HOLD: "hold",
            FINVIZ_ANALYSIS.HOLD_WORSE: "holdworse",
            FINVIZ_ANALYSIS.SELL: "sell",
            FINVIZ_ANALYSIS.SELL_WORSE: "sellworse",
            FINVIZ_ANALYSIS.STRONG_SELL: "strongsell"
        }
        return f"?v=111&f=an_recom_{filters.get(analysis,'')}"
    

load_dotenv(override=True)

api_key = os.getenv("FINVIZ_API")


import requests


URL = "https://elite.finviz.com/export.ashx?[{}]&auth={}"
filter = FINVIZ_ANALYSIS.filter(FINVIZ_ANALYSIS.HOLD)
response = requests.get(URL.format(filter, api_key))
print(response.status_code)
csv = io.StringIO(response.content.decode('utf-8'))
df = pd.read_csv(csv)
assets_list = df["Ticker"].to_list()
print(len(assets_list))