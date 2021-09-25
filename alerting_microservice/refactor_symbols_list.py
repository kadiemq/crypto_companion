def refactor_symbols_list(list):
    refactored_list = []
    
    for item in list:
        item = item.lower()
        refactored_list.append(item + '@kline_1m')

    return refactored_list