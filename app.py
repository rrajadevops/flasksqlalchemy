from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.item import Item, ItemList

from security import authenticate, identity
from resources.user import UserRegister

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Flase
app.secret_key = 'raja'
api = Api(app)

@app.before_first_request
def create_db():
    db.create_all()

jwt = JWT(app, authenticate, identity) #/auth



api.add_resource(Item, '/item/<string:name>')  #127.0.0.1:5000/item/pen
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)