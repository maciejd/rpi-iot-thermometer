from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sensors import DHT11, DS18b20
import config
import threading

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app=app)
class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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
    sensor_data = SensorData(temperature=temperature, humidity=humidity)
    print(f'send_data: {sensor_data}')
    # add new data
    db.session.add(sensor_data)
    db.session.commit()


@app.route("/home")
def hello():
    ds18b20_temperature = DS18b20.get_temperature_from_ds18b20()
    dht11_temperature, dht11_humidity = DHT11.read_from_DHT11().values()
    print(f'dht11_temperature:{dht11_temperature}')
    return render_template('home.html', ds18b20_temperature=ds18b20_temperature, dht11_temperature=dht11_temperature, dht11_humidity=dht11_humidity)
    return 'Hello'


@app.route("/refresh_data", methods=['GET'])
def refresh_data():
    ds18b20_temperature = DS18b20.get_temperature_from_ds18b20()
    dht11_temperature, dht11_humidity = DHT11.read_from_DHT11().values()
    return jsonify(
        {
            "temperature_DS18B20": ds18b20_temperature,
            "temperature_DHT11": dht11_temperature,
            "humidity_DHT11": dht11_humidity
        }
    )

# if __name__ == '__main__':
#     # send_data_repeat()
#     app.run(port='5050', debug=True)
