from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from src.item import Item, ItemList
from src.security import authenticate, identity
from src.user import UserRegister

app = Flask(__name__)
app.secret_key = 'secret'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/item/devowner
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

app.run(port=5000)
