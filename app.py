from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sensors import DHT11, DS18b20
import config
import threading

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app=app)

# 24h 温度 + 湿度
class SensorDataHour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hour = db.Column(db.Integer)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Integer)
    
    def __repr__(self) -> str:
        return f'hour: {self.hour} h, temperature: {self.temperature} *C, humidity:{self.humidity} %'


# 每天温度
class SensorDataDaily(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Integer)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Integer)
    
    def __repr__(self) -> str:
        return f'temperature: {self.temperature}, humidity:{self.humidity}'

db.drop_all()
db.create_all()

def send_data_repeat():
    threading.Timer(3, send_data_repeat).start()
    temperature = DS18b20.get_temperature_from_ds18b20()
    _, humidity = DHT11.read_from_DHT11().values()
    sensor_data = SensorDataHour(temperature=temperature, humidity=humidity)
    print(f'send_data: {sensor_data}')
    # add new data
    db.session.add(sensor_data)
    db.session.commit()


@app.route("/home")
def hello():
    ds18b20_temperature = DS18b20.get_temperature_from_ds18b20()
    _, dht11_humidity = DHT11.read_from_DHT11().values()
    return render_template('home.html', temperature=ds18b20_temperature, humidity=dht11_humidity)


# For Ajax
@app.route("/refresh_data", methods=['GET'])
def refresh_data():
    ds18b20_temperature = DS18b20.get_temperature_from_ds18b20()
    _, dht11_humidity = DHT11.read_from_DHT11().values()
    return jsonify(
        {
            "temperature": ds18b20_temperature,
            "humidity": dht11_humidity
        }
    )

# if __name__ == '__main__':
#     # send_data_repeat()
#     app.run(port='5050', debug=True)
