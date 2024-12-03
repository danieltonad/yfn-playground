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

# payload =   json.dumps({"filter":[{"left":"exchange","operation":"equal","right":"BYBIT"},{"left":"RSI|240","operation":"eless","right":30},{"left":"Stoch.K|240","operation":"eless","right":20},{"left":"Stoch.D|240","operation":"eless","right":20},{"left":"CCI20|240","operation":"eless","right":-100},{"left":"Recommend.Other|240","operation":"nequal","right":0.1},{"left":"W.R|240","operation":"eless","right":-80},{"left":"currency","operation":"equal","right":"USDT"}],"options":{"lang":"en"},"filter2":{"operator":"and","operands":[{"operation":{"operator":"or","operands":[{"expression":{"left":"type","operation":"in_range","right":["spot"]}}]}},{"operation":{"operator":"or","operands":[{"expression":{"left":"Recommend.Other|240","operation":"in_range","right":[0.1,0.5]}},{"expression":{"left":"Recommend.Other|240","operation":"in_range","right":[0.5,1]}}]}}]},"markets":["crypto"],"symbols":{"query":{"types":[]},"tickers":[]},"columns":["Recommend.All|240"],"range":[0,150]})
payload =   json.dumps({"filter":[{"left":"exchange","operation":"equal","right":"BYBIT"},{"left":"Perf.YTD","operation":"egreater","right":100},{"left":"Recommend.All|240","operation":"nequal","right":0.1},{"left":"Recommend.MA|240","operation":"nequal","right":0.1},{"left":"Recommend.Other|240","operation":"nequal","right":0.1},{"left":"currency","operation":"equal","right":"USDT"}],"options":{"lang":"en"},"filter2":{"operator":"and","operands":[{"operation":{"operator":"or","operands":[{"expression":{"left":"type","operation":"in_range","right":["spot"]}}]}},{"operation":{"operator":"or","operands":[{"expression":{"left":"Recommend.All|240","operation":"in_range","right":[0.1,0.5]}},{"expression":{"left":"Recommend.All|240","operation":"in_range","right":[0.5,1]}}]}},{"operation":{"operator":"or","operands":[{"expression":{"left":"Recommend.MA|240","operation":"in_range","right":[0.1,0.5]}},{"expression":{"left":"Recommend.MA|240","operation":"in_range","right":[0.5,1]}}]}},{"operation":{"operator":"or","operands":[{"expression":{"left":"Recommend.Other|240","operation":"in_range","right":[0.1,0.5]}},{"expression":{"left":"Recommend.Other|240","operation":"in_range","right":[0.5,1]}}]}}]},"markets":["crypto"],"symbols":{"query":{"types":[]},"tickers":[]},"columns":[],"range":[0,150]})

with Session() as session:
    res = session.post(url=url, data=payload, headers=headers)
    if res.status_code == 200:
        result = res.json()
        for dt in result.get("data"):
            # print(dt)
            print(dt["s"])

# {"filter":[{"left":"exchange","operation":"equal","right":"BYBIT"},{"left":"RSI|240","operation":"eless","right":30},{"left":"Stoch.K|240","operation":"eless","right":20},{"left":"Stoch.D|240","operation":"eless","right":20},{"left":"CCI20|240","operation":"eless","right":-100},{"left":"W.R|240","operation":"eless","right":-80},{"left":"currency","operation":"equal","right":"USDT"}],"options":{"lang":"en"},"filter2":{"operator":"and","operands":[{"operation":{"operator":"or","operands":[{"expression":{"left":"type","operation":"in_range","right":["spot"]}}]}}]},"markets":["crypto"],"symbols":{"query":{"types":[]},"tickers":[]},"columns":["base_currency_logoid","currency_logoid","name","close|240","change|240","change_abs|240","high|240","low|240","volume|240","24h_vol|5","24h_vol_change|5","Recommend.All|240","exchange","description","type","subtype","update_mode|240","pricescale","minmov","fractional","minmove2"],"sort":{"sortBy":"total_shares_diluted","sortOrder":"asc"},"price_conversion":{"to_symbol":false},"range":[0,150]}
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
