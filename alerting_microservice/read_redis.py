import redis

def read_redis(table_name):
    r = redis.Redis(host='', port=6379, db=0)
    return r.get(table_name)