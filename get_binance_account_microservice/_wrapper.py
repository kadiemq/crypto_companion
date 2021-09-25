from decrypt import decrypt
from write_to_redis import write_to_redis
from binance.client import Client
from profitability import profitability
from coin_cost import coin_cost
import os
from recent_orders import get_orders
from raw_coins_list import get_raw_coin_list
import time

def microservice_wrapper(body):
    start = time.time()
    data = eval(body)

    user_id = data['user_id']
    binance_public_key = decrypt(data['binance_public_key'])
    binance_secret_key = decrypt(data['binance_secret_key'])

    client = Client(binance_public_key, binance_secret_key)

    print(f'Recieved an order for user {user_id}')

    net_worth, coin_list = get_raw_coin_list(client)

    for coin in coin_list:
        if not coin['asset'] == 'USDT':
            coin_amount = float(coin['free']) + float(coin['locked'])
            coin['recent_orders'] = get_orders(client, coin['symbol'], coin_amount, coin['current_price'])
            coin['cost_per_token'] = coin_cost(coin['recent_orders'])
            coin['profitability'], coin['profitability_percentage'] = profitability(coin['cost_per_token'], coin['current_price'], coin['free'], coin['locked'])

    data_redis = {'net_worth': net_worth,'coin_list': coin_list}
    table_name = f'{user_id}_coin_list'

    write_to_redis(table_name, data_redis, 60)

    end = time.time()
    print(f"Runtime of microservice for user {user_id}: {end - start}")