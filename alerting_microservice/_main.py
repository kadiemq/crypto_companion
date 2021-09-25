import time

import pandas as pd

from database_funcs import get_matching_alerts, db_get_symbols_list
from get_prices import get_prices
from process_row import process_row

rows = pd.DataFrame()


def loop_matching_symbols_rows(row):
    global rows
    rows = rows.append(get_matching_alerts(row['symbol'], row['price']))


def run_microservice():
    start = time.time()

    all_symbols = get_prices()
    db_symbols_list = db_get_symbols_list()

    matching_symbols = all_symbols[all_symbols['symbol'].isin(db_symbols_list)]

    matching_symbols.apply(loop_matching_symbols_rows, axis=1)

    print(rows)

    rows.apply(process_row, axis=1)

    end = time.time()
    print(f"Runtime of loop: {end - start}")


if __name__ == '__main__':
    run_microservice()

