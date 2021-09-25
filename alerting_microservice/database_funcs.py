import psycopg2
import pandas as pd
import time

def open_connection():
    conn = psycopg2.connect(user="",
                            password="",
                            host="",
                            port="",
                            database="")

    return conn


def db_get_symbols_list():
    start = time.time()
    conn = open_connection()

    cur = conn.cursor()
    cur.execute("select distinct symbol from alerts_model3")
    records = cur.fetchall()
    result = [r[0] for r in records]

    conn.close()
    end = time.time()
    print(f"Runtime of get_symbols_list: {end - start}")
    return result


def get_all_alerts():
    conn = open_connection()

    cur = conn.cursor()
    cur.execute("select * from alerts_model")
    records = cur.fetchall()

    df = pd.DataFrame(records, columns=['id', 'type', 'symbol', 'trigger', 'price', 'quantity', 'direction', 'action', 'user_id', 'user_email', 'message', 'done', 'prder_type', 'time_in_fore'])
    conn.close()
    return df


def get_matching_alerts(symbol, trigger):
    conn = open_connection()

    cur = conn.cursor()
    cur.execute(f"select * from alerts_model where (symbol = '{symbol}' and direction = 'ABOVE' and trigger < '{trigger}' and done = 'false') or (symbol = '{symbol}' and direction = 'BELOW' and trigger > '{trigger}' and done = 'false')")
    records = cur.fetchall()

    df = pd.DataFrame(records, columns=['id', 'type', 'symbol', 'trigger', 'price', 'quantity', 'direction', 'action', 'user_id', 'user_email', 'message', 'done', 'prder_type', 'time_in_fore'])

    cur.execute(f"update alerts_model3 set done = 'true' where (symbol = '{symbol}' and direction = 'ABOVE' and trigger < '{trigger}' and done = 'false') or (symbol = '{symbol}' and direction = 'BELOW' and trigger > '{trigger}' and done = 'false')")
    conn.commit()
    conn.close()
    return df
