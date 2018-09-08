from flask_restful import Resource, reqparse
from models.UserModel import UserModel
from crypt_password import Crypto

parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)

class UserRegister(Resource):

    def post(self):
        data = parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'Error':'{} user alredy exist'.format(data['username'])}, 200
        user = UserModel(username = data['username'], password = Crypto.generate_hash(data['password']))
        try:
            user.save_to_db()
            return {
                'message': 'User {} was created'.format( data['username'])
            }, 200
        except:
            return {'message': 'Something went wrong'}, 500

class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if not user:
            return {'Error': '{} user does not exist'.format(data['username'])}, 404
        if Crypto.verify_hash(data['password'],user.password):
            return {'Msg': 'Logged'}, 200
        else:
            return {'msg': 'wrong credentials'}, 200

class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}


class SecretTestResource(Resource):
    def get(self):
        return {'msf':'xxd'}













class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}

class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}