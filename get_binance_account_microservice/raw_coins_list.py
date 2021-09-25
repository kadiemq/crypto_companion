

def get_raw_coin_list(client):
    
    coin_list = []
    net_worth = 0


    coin_list_raw = client.get_account()
    balances = coin_list_raw['balances']

    for coin in balances:
        coin_amount = float(coin['free']) + float(coin['locked'])
        asset = coin['asset']
        if not coin_amount > 0:
            continue

        if asset == 'USDT':
            coin['price'] = 1
            coin['value'] = coin_amount

            coin_list.append(coin)
            net_worth += coin_amount
            continue

        try:
            avg_price = float(client.get_avg_price(symbol=asset + 'USDT')['price'])
            asset_value = coin_amount * avg_price

            if asset_value > 1:
                coin['current_price'] = avg_price
                coin['current_value'] = asset_value
                coin['symbol'] = asset + 'USDT'

                coin_list.append(coin)
                net_worth += asset_value
        except:
            pass


    return net_worth, coin_list
