from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap4
from flask_moment import Moment


app = Flask('smart_home')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
bootstrap = Bootstrap4(app)
moment = Moment(app)

# Must
from smart_home import views, models, commands
