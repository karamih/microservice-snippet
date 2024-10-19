import os
import json
import pika

params = pika.URLParameters(os.getenv('MESSAGE_BROKER_URL'))

try:
    connection = pika.BlockingConnection(parameters=params)
    channel = connection.channel()

    channel.queue_declare('admin')


    def publish(method, body):
        properties = pika.BasicProperties(content_type=method)
        channel.basic_publish(exchange='',
                              routing_key='admin',
                              body=json.dumps(body),
                              properties=properties)


    print('Published from main...')

except Exception as e:
    print(f'Error {e}')
