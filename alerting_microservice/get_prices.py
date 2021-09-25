import requests
import pandas as pd
import time

url = 'https://api.binance.com/api/v3/ticker/price'
vars = []


def get_prices():
    # start = time.time()


    r = requests.get(url=url)
    # client.get_price
    data = r.json()

    df = pd.DataFrame(data, columns=['symbol', 'price'])


    # vars.append({'symbol': data['symbol'], 'value': data['price']})

    # end = time.time()
    # print(f"Runtime of get_prices: {end - start}")
    return df
