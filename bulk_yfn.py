import yfinance as yf
from typing import List, Tuple
import pandas as pd

def get_highest_weekly_volume_ever(assets: List[str]) -> List[Tuple[int, str]]:
    results = []
    try:
        # Download data for all tickers in one go
        data: pd.DataFrame = yf.download(assets, period="max", interval="1wk")
        print(type(data))
        for ticker in assets:
            try:
                # Select the data for the current ticker
                ticker_data = data.xs(ticker, level=1, axis=1)
                # Extract the 'Volume' column
                if 'Volume' in ticker_data:
                    volume_data = ticker_data['Volume'].dropna()
                    if not volume_data.empty:
                        volume_data = ticker_data['Volume']
                        highest_volume = volume_data.max()
                        highest_volume_date = volume_data.idxmax().to_pydatetime().strftime("%d-%m-%Y %H:%M:%S")
                        results.append({ticker: (highest_volume.item(), highest_volume_date)})
                    else:
                        results.append({ticker: (False, None)})
            except KeyError:
                results.append({ticker: (False, None)})

    except Exception as err:
        print(err)
        # log =  Logger()
        # log.app_log(title="HWVE_ERR", message=f"Unable to Fetch volume for assets: {assets}")
        results.append((False, None))
    return results

# Example usage
assets = ["BEKE","OMC","WSO.B","DKNG","PFG","BAM","AER","EDR","GPC","ESS","PKG","EC","STLD","WSM","SYF/PB","SYF/PA","MAA/PI","MAA","SYF","APTV","EXPE","WLK","J","ZBRA","ULTA","CNP","FOXA","FOX","DG","NTRSO","NRG","NTRS","CFG/PH","CFG/PE","SSNC","TS","CFG","MAS","LUV","EXPD","ZTO","UAL","VRSN","JBHT","AVTR","TME","SNAP","RYAN","DKS","AVY","LINE","FDS","IHG","MANH","BURL","CTRA","SUI","L","CRBG","ENTG","HRL","EBR","EBR.B","JHX","LPLA","IP","GEN","FNF","VIV","PSTG"]
results = get_highest_weekly_volume_ever(assets)
for result in results:
    print(result)
