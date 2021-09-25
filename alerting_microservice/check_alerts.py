from database_funcs import get_matching_alerts
from multiprocessing import Process
import time

def check_alerts(symbols):
    start = time.time()
    df = None
    for symbol in symbols:
        if df is None:
            df = get_matching_alerts(symbol['symbol'], symbol['value'])
        else:
            df = df.append(get_matching_alerts(symbol['symbol'], symbol['value']))

    end = time.time()
    print(f"Runtime of check_alerts: {end - start}")
    return df
