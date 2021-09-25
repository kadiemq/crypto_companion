import numpy as np

def get_orders(client, symbol, coin_amount, avg_price):
    trades_list = []
    coin_amount = coin_amount

    trades = np.array(client.get_all_orders(symbol=symbol))
    trades = trades[::-1]

    for trade in trades:
        executed_amount = trade['executedQty']
        if coin_amount * avg_price < 2:
            break

        if not float(executed_amount) > 0:
            continue

        if trade['side'] == 'BUY':
            coin_amount -= float(executed_amount)
        else:
            coin_amount += float(executed_amount)

        trades_list.append(trade)

    return trades_list