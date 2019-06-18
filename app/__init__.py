from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from flask_cors import CORS
from flask_mail import Mail

from app.db import db
from app.security import authenticate, identity
from app.models.user import UserModel

app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.cfg')
api = Api(app)
mail = Mail(app)

jwt = JWT(app, authenticate, identity)

from app.resources.contact import Contact

api.add_resource(Contact, '/contact')