import os
import pika
import json

params = pika.URLParameters(os.getenv("MESSAGE_BROKER_URL"))

try:
    connection = pika.BlockingConnection(parameters=params)

    channel = connection.channel()
    channel.queue_declare(queue='main')


    def publish(method, body):
        properties = pika.BasicProperties(method)

        channel.basic_publish(exchange='',
                              routing_key='main',
                              body=json.dumps(body),
                              properties=properties)

    print('published from admin...')

except Exception as e:
    print(f'Error {e}')
