import asyncio
from refactor_symbols_list import refactor_symbols_list
from process_row import process_row
from database_funcs import get_matching_alerts, db_get_symbols_list
import websockets

import time
import json
import sys


async def candle_stick_data(factored_symbols_list):
    url = "wss://stream.binance.com:9443/ws/" #steam address
    first_pair = factored_symbols_list[0]
    rest_of_pairs = factored_symbols_list[1:]
    async with websockets.connect(url+first_pair) as sock:
        pairs = {"method": "SUBSCRIBE", "params": rest_of_pairs,  "id": 1}
        pairs = json.dumps(pairs)

        await sock.send(pairs)
        print(f"> {pairs}")
        while True:
            start = time.time()
            resp = await sock.recv()
            resp = json.loads(resp)
            k = resp.get('k')

            if k is not None:
                rows = get_matching_alerts(k['s'], k['c'])
                # print(sys.getsizeof(str(rows)))
                rows.apply(process_row, axis=1)


            end = time.time()
            print(f"Runtime of loop: {end - start}")

if __name__ == '__main__':
    db_symbols_list = db_get_symbols_list()
    factored_symbols_list = refactor_symbols_list(db_symbols_list)
    asyncio.run(candle_stick_data(factored_symbols_list))
