from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from run import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
db = SQLAlchemy(app)
jwt = JWTManager(app)

@app.before_first_request
def create_tables():
    db.create_all()