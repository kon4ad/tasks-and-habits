from flask_restful import Resource

class UserRegister(Resource):
    def post(self):
        return "registered"

class UserLogin(Resource):
    def post(self):
        return "login"

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