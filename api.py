from flask import Flask, jsonify, abort, request
from flask.ext.sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)    

class Temps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temp = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

@app.route('/temp/', methods = ['GET'])
def index():
    t = Temps.query.order_by(Temps.id.desc()).first()
    return jsonify(temperature=t.temp, measured_at=t.timestamp)
