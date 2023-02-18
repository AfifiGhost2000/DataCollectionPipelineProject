from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DashboardDB.db'
app.config['SECRET_KEY'] = 'JJKjkdfkfhksdgkhsdfhkgfds80932497hbdv98098784321hjbhbvchjs19034000'


db = SQLAlchemy(app)

from application import routes


