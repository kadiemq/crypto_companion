import pika
from cryptography.fernet import Fernet
import os


def send_binance_account_microservice_rabbitmq(user_id, binance_public_key, binance_secret_key):
    conn = pika.BlockingConnection(pika.ConnectionParameters(''))
    channel = conn.channel()

    key = os.environ['encryption_key']
    f = Fernet(key)

    binance_public_key = f.encrypt(binance_public_key.encode())
    binance_secret_key = f.encrypt(binance_secret_key.encode())

    data = {"user_id": user_id, 'binance_public_key': binance_public_key, 'binance_secret_key': binance_secret_key}

    channel.basic_publish(exchange='', routing_key='binance_account_microservice', body=str(data))

    conn.close()
