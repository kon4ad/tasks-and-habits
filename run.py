from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)
import config, resources

api.add_resource(resources.UserRegister, "/register")
api.add_resource(resources.UserLogin, "/login")
api.add_resource(resources.SecretTestResource, "/content")
api.add_resource(resources.TokenRefresh, "/token/refresh")
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')

if __name__ == "__main__":
    app.run()