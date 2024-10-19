import os
import json
import pika
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from product.models import ProductModels

params = pika.URLParameters(os.getenv('MESSAGE_BROKER_URL'))

try:
    connection = pika.BlockingConnection(parameters=params)
    channel = connection.channel()

    channel.queue_declare('admin')


    def callback(ch, method, properties, body):
        print('data received in admin...')
        pk = json.loads(body)
        print(pk)
        if properties.content_type == 'product_liked':
            product = ProductModels.objects.get(id=pk)
            product.likes = product.likes + 1
            product.save()
            print('Product likes increased!')


    channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

    print('start consuming in admin...')

    channel.start_consuming()

except Exception as e:
    print(f'Error {e}')
