from flask import Flask
from flask_restful import Api
app = Flask(__name__)
api = Api(app)
import  data_base_config, resources

api.add_resource(resources.UserRegister, "/register")
api.add_resource(resources.UserLogin, "/login")
api.add_resource(resources.SecretTestResource, "/secret")
api.add_resource(resources.TokenRefresh, "/token/refresh")
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')

if __name__ == "__main__":
    app.run()