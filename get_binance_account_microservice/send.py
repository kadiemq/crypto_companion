# FOR TESTING PURPOSES 
# API KEYS MUST BE ENCRYPTED!




import pika

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()

data = {"user_id": 1, 
    'binance_public_key': b'', 
    'binance_secret_key': b''}
channel.basic_publish(exchange='', routing_key='binance_account_microservice', body=str(data))

conn.close()