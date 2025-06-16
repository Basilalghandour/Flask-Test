from flask import Flask
app = Flask(__name__)
from market import routes
from flask_sqlalchemy import SQLAlchemy
app.config['SECRET_KEY'] = '30867c65495ecc45f74fec30'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)
