from flask_restful import Resource, reqparse
from models.UserModel import UserModel
from crypt_password import Crypto
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)

def create_token(username):
    return {
        'access_token': create_access_token(username),
        'refresh_token': create_refresh_token(username)
    }

class UserRegister(Resource):

    def post(self):
        data = parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'Error':'{} user alredy exist'.format(data['username'])}, 200
        user = UserModel(username = data['username'], password = Crypto.generate_hash(data['password']))
        try:
            user.save_to_db()
            return create_token(data['username']), 200
        except:
            return {'message': 'Something went wrong'}, 500

class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if not user:
            return {'Error': '{} user does not exist'.format(data['username'])}, 404
        if Crypto.verify_hash(data['password'],user.password):
            return create_token(data['username']), 200
        else:
            return {'msg': 'wrong credentials'}, 200

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token': access_token}


class SecretTestResource(Resource):
    @jwt_required
    def get(self):
        return {'msf':'xxd'}













class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}

class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}