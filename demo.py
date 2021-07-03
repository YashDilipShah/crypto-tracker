import requests as r
import os
shiba_inu = os.path.join(os.getcwd(), 'shiba-inu.mp3')
shiba_inu_sell = os.path.join(os.getcwd(), 'shiba-inu-sell.mp3')
doge = os.path.join(os.getcwd(), 'doge-coin.mp3')
doge_sell = os.path.join(os.getcwd(), 'doge-coin-sell.mp3')

base = 'https://api.wazirx.com/'

#market_status = r.get(url = base + 'api/v2/market-status').json()

#market_tickers = r.get(url = base + 'api/v2/tickers').json()

shib_buy = 0.00064
shib_sell = 1
doge_buy = 20
doge_sell = 50 

while True:
    ticker = r.get(url = base + 'api/v2/tickers').json()
    
    shib = float(ticker['shibinr']['last'])
    doge = float(ticker['dogeinr']['last'])

    """
    
    if shib > shib_sell:
        os.system("{0} {1}".format("mpg123", shiba_inu_sell))
    elif shib < shib_buy:
        os.system("{0} {1}".format("mpg123", shiba_inu))
    

    
    if doge > doge_sell:
        os.system("{0} {1}".format("mpg123", doge_sell))
    elif doge < doge_buy:
        os.system("{0} {1}".format("mpg123", doge))
    """

    print(shib, doge)
    