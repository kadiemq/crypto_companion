import redis

def write_to_redis(table_name, data, ex):
    r = redis.Redis(host='', port=6379, db=0)
    r.set(table_name, str(data), ex=ex)