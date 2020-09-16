from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from apis.item import Item, ItemList
from apis.user import UserRegister
from src.security import authenticate, identity
from database.db import db


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/item/devowner
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
