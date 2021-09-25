from write_to_redis import write_to_redis
from refactor_symbols_list import refactor_symbols_list
from database_funcs import db_get_symbols_list

import time

def background_works():
    db_symbols_list = db_get_symbols_list()
    factored_symbols_list = refactor_symbols_list(db_symbols_list)
    write_to_redis('symbols_list', factored_symbols_list, 60)


def background_works_wrapper():
    while True:
        background_works()
        time.sleep(10)