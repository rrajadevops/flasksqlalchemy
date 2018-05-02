import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('password',
        type=str,
        required=True,
        help="This filed is can't empty!"
    )
    parser.add_argument('username',
        type=str,
        required=True,
        help="This filed is can't empty!"
    )
    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "Username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()


        connection.commit()
        connection.close()
        return {"message": "User created successfully!"}, 201
