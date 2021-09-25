def coin_cost(recent_orders):

    qty_sum = 0
    qty_by_price_sum = 0

    for order in recent_orders:
        if order['side'] == 'SELL':
            continue
        qty_sum += float(order['executedQty'])
        qty_by_price_sum += float(order['executedQty']) * float(order['price'])

    return qty_by_price_sum / qty_sum