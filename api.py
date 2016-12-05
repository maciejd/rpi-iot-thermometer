from flask import Flask, jsonify, abort, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import datetime, json

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
    since = datetime.datetime.now() - datetime.timedelta(hours=24)
    t = Temps.query.filter(Temps.timestamp >= since).all()
    return json.dumps([{"_id": i, "date": t[i].timestamp.strftime("%Y-%m-%d %H:%M"), "temp": t[i].temp}
        for i in range(len(t))])

@app.route('/')
def graph():
     since = datetime.datetime.now() - datetime.timedelta(hours=24)
     last24 = Temps.query.filter(Temps.timestamp >= since)
     now = Temps.query.order_by(Temps.id.desc()).first()
     max = Temps.query.with_entities(func.max(Temps.temp).label("temp"), Temps.timestamp).first()
     avg = last24.with_entities(func.avg(Temps.temp).label("temp")).first()
     min = Temps.query.with_entities(func.min(Temps.temp).label("temp"), Temps.timestamp).first()
     return render_template("index.html", now=now, max=max, avg=avg, min=min)

