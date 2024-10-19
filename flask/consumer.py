import os
import pika
import json
from app import ProductModel, db, app

params = pika.URLParameters(os.getenv("MESSAGE_BROKER_URL"))

try:
    connection = pika.BlockingConnection(parameters=params)
    channel = connection.channel()

    channel.queue_declare('main')


    def callback(ch, method, properties, body):
        print('data received in main...')
        data = json.loads(body)
        print(data)

        with app.app_context():
            if properties.content_type == 'product_created':
                product = ProductModel(id=data['id'], title=data['title'], image=data['image'])
                db.session.add(product)
                db.session.commit()

            elif properties.content_type == 'product_updated':
                product = ProductModel.query.get(data['id'])
                product.title = data['title']
                product.image = data['image']
                db.session.commit()

            elif properties.content_type == 'product_deleted':
                product = ProductModel.query.get(data)
                db.session.delete(product)
                db.session.commit()


    channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

    print('start consuming in main...')

    channel.start_consuming()

except Exception as e:
    print(f'Error {e}')
