def profitability(cost_per_token, current_price, free_stock, locked_stock):
    total_stock = float(free_stock) + float(locked_stock)

    current_value = current_price * total_stock
    cost_price_value = cost_per_token * total_stock

    profitability_value = current_value - cost_price_value
    profitability_percentage = (current_value / cost_price_value) - 1

    return profitability_value, profitability_percentage