from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app.config['SECRET_KEY'] = '30867c65495ecc45f74fec30'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from market import routes

