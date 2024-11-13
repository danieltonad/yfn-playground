import yfinance as yf
import pandas as pd


def calculate_relative_strength(ticker, benchmark_ticker="SPY", period="2y"):
    try:
        stock_data = yf.Ticker(ticker).history(period=period)["Close"]
        benchmark_data = yf.Ticker(benchmark_ticker).history(period=period)["Close"]

        if stock_data.empty or benchmark_data.empty:
            return None, None

        def quarters_perf(closes: pd.Series, n: int) -> float:
            """Calculates cumulative performance over the last n quarters."""
            length = min(len(closes), n*int(252/4))
            prices = closes.tail(length)
            pct_chg = prices.pct_change().dropna()
            perf_cum = (pct_chg + 1).cumprod() - 1
            return perf_cum.tail(1).item()

        def strength(closes: pd.Series) -> float:
            """Calculates weighted performance over the last year."""
            q1_perf = quarters_perf(closes, 1)
            q2_perf = quarters_perf(closes, 2)
            q3_perf = quarters_perf(closes, 3)
            q4_perf = quarters_perf(closes, 4)
            return 0.4 * q1_perf + 0.2 * q2_perf + 0.2 * q3_perf + 0.2 * q4_perf
        
        # Calculate strengths
        stock_strength = strength(stock_data)
        benchmark_strength = strength(benchmark_data)
        
        # Calculate RS Score
        rs_score = (1 + stock_strength) / (1 + benchmark_strength) * 100

        return round(stock_strength, 4), round(rs_score, 2)

    except Exception as err:
        print(err)
        return None, None



# stock_ticker = 'SFST'  # Replace with your desired stock ticker
# rs_rating = calculate_relative_strength(stock_ticker)
# print(f"RS Rating for {stock_ticker}: {rs_rating}")


def bulk_test():
    stocks = ["AAPL","MSFT","NVDA","AMZN","GOOG","GOOGL","META","BRK.B","BRK.A","AVGO","TSLA","TSM","WMT","JPM/PL","JPM/PK","JPM/PD","JPM/PJ","JPM/PC","JPM/PM","JPM","V","XOM","ORCL","MA","PG","COST","HD","ASML","NFLX","KO","BAC/PN","BAC/PM","BML/PH","BAC/PO","BAC/PE","BAC/PK","BAC/PQ","BML/PJ","BML/PL","BAC/PS","BAC/PL","BAC/PB","MER/PK","BAC/PP","BML/PG","BAC","SAP","CVX","CRM","AMD","TM","TMUS","PEP","ADBE","LIN","BABA","MCD","SHEL","ACN","CSCO","GE","IBM","AXP","BX","PM","VZ","CAT","QCOM","TXN","NOW","WFC/PD","WFC/PZ","WFC/PL","WFC/PC","WFC/PA","WFC/PY","WFC","INTU","RY","NEE","NEE/PS","NEE/PR","DIS","MS/PP","MS/PI","MS/PE","MS/PL","MS/PA","MS/PK","MS/PO","MS/PQ","MS/PF","MS","HSBC","AMAT","TTE","UBER","SPGI","UL","HDB","RTX","CMCSA","PDD","GS","GS/PD","GS/PA","GS/PC","ARM","T","TBC","T/PC","TBB","T/PA","UNP","PGR","LOW","BHP","BKNG","BLK","LMT","HON","TJX","ETN","NKE","BUD","COP","ANET","PLD","MUFG","SCHW/PJ","SCHW/PD","KKR","SCHW","CB","SONY","C","RACE","RIO","ADP","ADI","DE","UPS","PANW","IBN","TD","AMT","MMC","MELI","SBUX","MU","LRCX","KLAC","SHOP","FI","INTC","MDLZ","SOJC","SOJE","SOJD","SO","UBS","BA","SHW","INFY","PBR","PBR.A","ICE","RELX","DUK","DUKB","DUK/PA","ENB","SCCO","TT","BP","MO","MCO","DELL","CL","BTI","EQIX","ABNB","GD","WM","SMFG","CTAS","CEG","PLTR","CP","PH","PYPL","TDG","APH","CMG","BN","SAN","CME","SNPS","WELL","NOC","TRI","ITW","DEO","AON","MMM","MSI","SPOT","CVS","CNI","CDNS","CNQ","CARR","ECL","PNC","EOG","TGT","APO","NU","APOS","APO/PA","USB/PR","USB/PP","USB/PS","USB/PA","USB/PQ","USB/PH","CRWD","USB","FCX","EQNR","GEV","MAR","NGG","BNS","CSX","ORLY","APD","BMO","FDX","WDAY","NEM","RSG","EPD","PSA/PP","PSA/PL","PSA/PN","PSA/PH","PSA/PK","PSA/PQ","PSA/PI","PSA/PR","PSA/PF","PSA/PJ","PSA/PG","PSA/PO","PSA","PSA/PS","PSA/PM","CRH","BBVA","MRVL","MCK","DHI","AJG","AFL","SLB","ING","EMR","ITUB","NXPI","DASH","FTNT","ROP","CM","ADSK","IBKR","MET","MET/PF","MET/PE","MET/PA","HLT","COF/PK","COF/PN","COF/PL","COF/PJ","COF/PI","TFC/PI","TFC/PR","TFC/PO","WMB","COF","NSC","TFC","OKE","ET/PI","SPG","SPG/PJ","ET","TTD","O/P","O","MPC","FANG","TRV","PSX","URI","AEP","SE","BK","DLR","DLR/PK","DLR/PL","DLR/PJ","NTES","SREA","SRE","HMC","AZO","MFC","PCAR","MNST","GWW","GM","KDP","CCI","CHTR","AMX","MFG","ROST","ALL/PB","ALL/PJ","ALL/PH","ALL/PI","JCI","CPRT","E","ALL","LEN","LEN.B","KMI","TRP","LYG","SU","HLN","PAYX","D","KMB","VALE","AIG","OXY","FICO","WCN","MPLX","STZ","AMP","RCL","STLA","JD","FIS","TEL","CPNG","MPWR","LHX","CMI","KVUE","MSCI","PWR","BCS","FLUT","COR","PEG","ODFL","APP"]
    results = []
    for stock in stocks[:10]:
        ticker = str(stock).replace("/", "-").replace(".", "-")
        try:
            strength, score = calculate_relative_strength(stock)
            if score is not None:
                results.append({"Ticker": ticker, "Strength": strength, "Score": score})
                print(f"{ticker} {score} {strength}"  ,end="\r")
            
        except:
            pass
    
    # Create a DataFrame
    df = pd.DataFrame(results)
    
    # Calculate percentile rank based on RS Score
    df["Rating"] = df["Score"].rank(pct=True) * 100
    df["Rating"] = df["Rating"].astype(int)
    
    # Sort by RS Score descending
    df = df.sort_values(by="Score", ascending=False).reset_index(drop=True)
    
    print(df)
    
    for index, row in df.iterrows():
        print(f"{row['Ticker']}, {row['Strength']}, {row['Score']},  {row['Rating']}")

    




bulk_test()