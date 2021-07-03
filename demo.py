import requests as r

base = 'https://api.wazirx.com/'

#market_status = r.get(url = base + 'api/v2/market-status').json()

#market_tickers = r.get(url = base + 'api/v2/tickers').json()

while True:
    ticker = r.get(url = base + 'api/v2/tickers').json()
    shib = ticker['shibinr']['last']
    doge = ticker['dogeinr']['last']
    print(shib, doge)