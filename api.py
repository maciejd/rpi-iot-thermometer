from flask import Flask, jsonify, abort, request, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime
import json

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

@app.route('/data/')
def data():
    t = Temps.query.all()
    return json.dumps([{"_id": i, "date": t[i].timestamp.strftime("%Y-%m-%d %H:%M"), "temp": t[i].temp}
        for i in range(len(t))])

@app.route('/')
def graph():
     return render_template("index.html")
