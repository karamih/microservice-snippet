import os
import json
from dataclasses import dataclass
import requests
from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import UniqueConstraint
from producer import publish

app = Flask('__name__')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://' \
                                        f'{os.getenv("DATABASE_USER")}:' \
                                        f'{os.getenv("DATABASE_PASSWORD")}@' \
                                        f'{os.getenv("DATABASE_HOST")}:' \
                                        f'{os.getenv("DATABASE_PORT")}/' \
                                        f'{os.getenv("DATABASE_NAME")}'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@dataclass
class ProductModel(db.Model):
    id: int
    title: str
    image: str
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(50))
    image = db.Column(db.String(200))


@dataclass
class ProductUserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route("/")
def index():
    return f'Hi this is working and this is debug mode: {os.getenv("DEBUG")} that equal {os.getenv("DEBUG") == "1"} ' \
           f'and db information: {app.config["SQLALCHEMY_DATABASE_URI"]}'


@app.route("/api/products")
def products_list():
    return jsonify(ProductModel.query.all())


@app.route("/api/products/<int:pk>/likes", methods=["POST"])
def like_post(pk):
    req = requests.get('http://django:8000/api/user')
    print(f'request details: {req}')
    print(f'status code: {req.status_code}')

    result = req.json()

    try:
        product_user = ProductUserModel(user_id=result['id'], product_id=pk)
        db.session.add(product_user)
        db.session.commit()

        publish('product_liked', pk)

        return jsonify({'detail': 'success'})
    except Exception as e:
        abort('400', 'You already liked this product.')


if __name__ == "__main__":
    app.run(debug=os.getenv('DEBUG') == '1', host='0.0.0.0')
