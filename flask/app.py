import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import UniqueConstraint

app = Flask('__name__')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://' \
                                        f'{os.getenv("DATABASE_USER")}:' \
                                        f'{os.getenv("DATABASE_PASSWORD")}@' \
                                        f'{os.getenv("DATABASE_HOST")}:' \
                                        f'{os.getenv("DATABASE_PORT")}/' \
                                        f'{os.getenv("DATABASE_NAME")}'
print(app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class ProductModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(50))
    image = db.Column(db.String(200))


class ProductUserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route("/")
def index():
    return f'Hi this is working and this is debug mode: {os.getenv("DEBUG")} that equal {os.getenv("DEBUG") == "1"} ' \
           f'and db information: {app.config["SQLALCHEMY_DATABASE_URI"]}'


if __name__ == "__main__":
    app.run(debug=os.getenv('DEBUG') == '1', host='0.0.0.0')
