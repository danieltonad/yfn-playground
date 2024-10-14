from requests import Session
import json

url = "https://scanner.tradingview.com/crypto/scan"
headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json",
            "Cookie": "cookiePrivacyPreferenceBannerProduction=notApplicable; cookiesSettings={\"analytics\":true,\"advertising\":true}; _ga=GA1.1.2130486263.1722864702; g_state={\"i_p\":1725379077165,\"i_l\":3}; __gads=ID=7afc0abfd7dd5138:T=1725277307:RT=1725277307:S=ALNI_MZJvj-NS22fATM7KQmyJs4pXEh9fg; __gpi=UID=00000ee700db4bf9:T=1725277307:RT=1725277307:S=ALNI_MZ3hrbLS7mOZr_BhxWp3ynM4lekXA; __eoi=ID=cbdf53827138eeae:T=1725277307:RT=1725277307:S=AA-AfjaGV--1jj7q51zuqsRJfzT5; device_t=NGJ1UToy.DwU15eVUNM2ifl7yeShyBfycs-Kv2cB6L9IZo7IT554; sessionid=lxfxelapcz4wsjwifihma6umoq29sclz; sessionid_sign=v3:FfCCyuvPYN9XUdOsaCj/GiXZT46y3ZNKSb1DaHIfC6U=; png=352ff9a1-4518-4f67-ba13-87f544c1f6be; etg=352ff9a1-4518-4f67-ba13-87f544c1f6be; cachec=352ff9a1-4518-4f67-ba13-87f544c1f6be; tv_ecuid=352ff9a1-4518-4f67-ba13-87f544c1f6be; _sp_id.cf1a=e5c9d694-02bc-4600-9e2a-239d5904053b.1722864700.5.1725277884.1724774303.8d0e12f9-5237-464b-ac46-f665db3ac112; _ga_YVVRYGL0E0=GS1.1.1725277298.6.1.1725280156.47.0.0",
            "Origin": "https://www.tradingview.com",
            "Referer": "https://www.tradingview.com/",
            "Sec-Ch-Ua": "\"Microsoft Edge\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
            "X-Language": "en",
            "X-Requested-With": "XMLHttpRequest"
        }

payload =   json.dumps({"filter":[{"left":"exchange","operation":"equal","right":"KUCOIN"}, {"left":"close","operation":"crosses_above","right":"EMA10"},{"left":"currency","operation":"equal","right": "USDT"}], "options": {"lang": "en"}, "filter2": {"operator": "and", "operands": [{"operation": {"operator": "or", "operands": [{"expression": {"left": "type", "operation": "in_range", "right": ["spot"]}}]}}]}, "markets": ["crypto"], "symbols": {"query": {"types": []}, "tickers": []}, "columns": ["base_currency_logoid", "currency_logoid"], "range": [0, 300]})
# payload = json.dumps({"filter":[{"left":"exchange","operation":"equal","right":"KUCOIN"},{"left":"EMA10","operation":"crosses_below","right":"EMA20"},{"left":"currency","operation":"equal","right":"USDT"}],"options":{"lang":"en"},"filter2":{"operator":"and","operands":[{"operation":{"operator":"or","operands":[{"expression":{"left":"type","operation":"in_range","right":["spot"]}}]}}]},"markets":["crypto"],"symbols":{"query":{"types":[]},"tickers":[]},"columns":["base_currency_logoid","currency_logoid"],"range":[0,300]})
with Session() as session:
    res = session.post(url=url, data=payload, headers=headers)
    if res.status_code == 200:
        result = res.json()
        for dt in result.get("data"):
            print(dt["s"])
    # print(res.text)


# 1m -> 1
# 5m -> 5
# 15m -> 15
# 30m -> 30
# 1h -> 60
# 2h -> 120
# 4h -> 240
# 1d -> 
# 1w -> 1W
# 1w -> 1W

#      {"filter":[{"left":"exchange","operation":"equal","right":"KUCOIN"},{"left":"close|15","operation":"crosses","right":"EMA10|15"},{"left":"currency","operation":"equal","right":"USDT"}],"options":{"lang":"en"},"filter2":{"operator":"and","operands":[{"operation":{"operator":"or","operands":[{"expression":{"left":"type","operation":"in_range","right":["spot"]}}]}}]},"markets":["crypto"],"symbols":{"query":{"types":[]},"tickers":[]},"columns":["base_currency_logoid","currency_logoid","name","Recommend.Other|15","ADX|15","AO|15","ATR|15","CCI20|15","MACD.macd|15","MACD.signal|15","Mom|15","RSI|15","Stoch.K|15","Stoch.D|15","description","type","subtype","update_mode|15","exchange","ADX DI|15","ADX-DI|15","ADX DI[1]|15","ADX-DI[1]|15","AO[1]|15","AO[2]|15","CCI20[1]|15","Mom[1]|15","RSI[1]|15","Stoch.K[1]|15","Stoch.D[1]|15"],"sort":{"sortBy":"Mom|15","sortOrder":"desc"},"price_conversion":{"to_symbol":false},"range":[0,150]}: 
# [1m] {"filter":[{"left":"exchange","operation":"equal","right":"KUCOIN"},{"left":"EMA10|1","operation":"crosses_above","right":"EMA20|1"},{"left":"currency","operation":"equal","right":"USDT"}],"options":{"lang":"en"},"filter2":{"operator":"and","operands":[{"operation":{"operator":"or","operands":[{"expression":{"left":"type","operation":"in_range","right":["spot"]}}]}}]},"markets":["crypto"],"symbols":{"query":{"types":[]},"tickers":[]},"columns":["base_currency_logoid","currency_logoid","name","close|1","change|1","volume|1","24h_vol|5","24h_vol_change|5","Recommend.All|1","exchange","Perf.Y","Perf.YTD","relative_volume_10d_calc|1","relative_volume_intraday|5","total_shares_diluted","total_shares_outstanding","description","type","subtype","update_mode|1","pricescale","minmov","fractional","minmove2"],"sort":{"sortBy":"change|1","sortOrder":"desc"},"price_conversion":{"to_symbol":false},"range":[0,150]}:
# [5m] {"filter":[{"left":"exchange","operation":"equal","right":"KUCOIN"},{"left":"EMA10|5","operation":"crosses_above","right":"EMA20|5"},{"left":"currency","operation":"equal","right":"USDT"}],"options":{"lang":"en"},"filter2":{"operator":"and","operands":[{"operation":{"operator":"or","operands":[{"expression":{"left":"type","operation":"in_range","right":["spot"]}}]}}]},"markets":["crypto"],"symbols":{"query":{"types":[]},"tickers":[]},"columns":["base_currency_logoid","currency_logoid","name","close|5","change|5","volume|5","24h_vol|5","24h_vol_change|5","Recommend.All|5","exchange","Perf.Y","Perf.YTD","relative_volume_10d_calc|5","relative_volume_intraday|5","total_shares_diluted","total_shares_outstanding","description","type","subtype","update_mode|5","pricescale","minmov","fractional","minmove2"],"sort":{"sortBy":"change|5","sortOrder":"desc"},"price_conversion":{"to_symbol":false},"range":[0,150]}: 
# [15m] {"filter":[{"left":"exchange","operation":"equal","right":"KUCOIN"},{"left":"EMA10|15","operation":"crosses_above","right":"EMA20|15"},{"left":"currency","operation":"equal","right":"USDT"}],"options":{"lang":"en"},"filter2":{"operator":"and","operands":[{"operation":{"operator":"or","operands":[{"expression":{"left":"type","operation":"in_range","right":["spot"]}}]}}]},"markets":["crypto"],"symbols":{"query":{"types":[]},"tickers":[]},"columns":["base_currency_logoid","currency_logoid","name","close|5","change|5","volume|5","24h_vol|5","24h_vol_change|5","Recommend.All|5","exchange","Perf.Y","Perf.YTD","relative_volume_10d_calc|5","relative_volume_intraday|5","total_shares_diluted","total_shares_outstanding","description","type","subtype","update_mode|5","pricescale","minmov","fractional","minmove2"],"sort":{"sortBy":"change|5","sortOrder":"desc"},"price_conversion":{"to_symbol":false},"range":[0,150]}: 
# [30m] {"filter":[{"left":"exchange","operation":"equal","right":"KUCOIN"},{"left":"EMA10|30","operation":"crosses_above","right":"EMA20|30"},{"left":"currency","operation":"equal","right":"USDT"}],"options":{"lang":"en"},"filter2":{"operator":"and","operands":[{"operation":{"operator":"or","operands":[{"expression":{"left":"type","operation":"in_range","right":["spot"]}}]}}]},"markets":["crypto"],"symbols":{"query":{"types":[]},"tickers":[]},"columns":["base_currency_logoid","currency_logoid","name","close|30","change|30","volume|30","24h_vol|5","24h_vol_change|5","Recommend.All|30","exchange","Perf.Y","Perf.YTD","relative_volume_10d_calc|30","relative_volume_intraday|5","total_shares_diluted","total_shares_outstanding","description","type","subtype","update_mode|30","pricescale","minmov","fractional","minmove2"],"sort":{"sortBy":"change|30","sortOrder":"desc"},"price_conversion":{"to_symbol":false},"range":[0,150]}
# [1hr] {"filter":[{"left":"exchange","operation":"equal","right":"KUCOIN"},{"left":"EMA10|60","operation":"crosses_above","right":"EMA20|60"},{"left":"currency","operation":"equal","right":"USDT"}],"options":{"lang":"en"},"filter2":{"operator":"and","operands":[{"operation":{"operator":"or","operands":[{"expression":{"left":"type","operation":"in_range","right":["spot"]}}]}}]},"markets":["crypto"],"symbols":{"query":{"types":[]},"tickers":[]},"columns":["base_currency_logoid","currency_logoid","name","close|60","change|60","volume|60","24h_vol|5","24h_vol_change|5","Recommend.All|60","exchange","Perf.Y","Perf.YTD","relative_volume_10d_calc|60","relative_volume_intraday|5","total_shares_diluted","total_shares_outstanding","description","type","subtype","update_mode|60","pricescale","minmov","fractional","minmove2"],"sort":{"sortBy":"change|60","sortOrder":"desc"},"price_conversion":{"to_symbol":false},"range":[0,150]}: 