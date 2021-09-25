from multiprocessing import Process
import pika
import os

from secret_key import get_secret
from _wrapper import microservice_wrapper

connection = pika.BlockingConnection(pika.ConnectionParameters(host=''))
channel = connection.channel()
channel.queue_declare('binance_account_microservice')

def cb(ch, method, properties, body):

    p = Process(target=microservice_wrapper, args=(body,))
    p.start()
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume('binance_account_microservice', on_message_callback=cb)

if __name__ == '__main__':
    print('Started get binance account microservice.....')
    print('Getting encrption key.....')
    os.environ['encryption_key'] = get_secret()
    print('Started consuming messages: "binance_account_microservice"')
    channel.start_consuming()
