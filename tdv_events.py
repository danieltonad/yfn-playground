import requests
from datetime import datetime, timedelta, timezone



def minutes_left(target_time_str):
    target_time = datetime.fromisoformat(target_time_str.replace("Z", "+00:00"))
    current_time = datetime.now(timezone.utc)
    time_difference = target_time - current_time
    minutes = int(time_difference.total_seconds() / 60)
    return minutes

def get_dates(days):
    current_time = datetime.now(timezone.utc)
    next_time = current_time + timedelta(days=days)
    current_date_str = current_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    next_date_str = next_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    
    return current_date_str, next_date_str


# def 
url = "https://economic-calendar.tradingview.com/events"
params = {
    "from": "2024-12-20T10:59:49.000Z",
    "to": "2024-12-22T10:59:49.000Z",
    "countries": "US,EU,CN,GB",
}

headers = {
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "origin": "https://www.tradingview.com",
    "referer": "https://www.tradingview.com/",
    "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
}

response = requests.get(url, headers=headers, params=params)
result = response.json()
if response.status_code == 200 and result.get("status") == 'ok':
    data = result.get("result")
    events = [event for event in data if int(event.get("importance")) > 0]
    for event in events:
        date = event.get("date")    
        ticker = event.get("ticker")
        minutes_remaining = minutes_left(date)
        print(f"{ticker} -> {minutes_remaining}")


# print(events)
    
print(get_dates(8))