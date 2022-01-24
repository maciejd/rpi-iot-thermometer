from smart_home import app
from flask import render_template, jsonify
from smart_home.sensors.DS18b20 import get_temperature_from_ds18b20
from smart_home.sensors.DHT11 import read_from_DHT11


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    temperature = get_temperature_from_ds18b20()
    _, humidity = read_from_DHT11().values()
    if temperature is not None and humidity is not None:
        return render_template('home.html', temperature=temperature, humidity=humidity)


# For Ajax
@app.route("/refresh_data", methods=['GET'])
def refresh_data():
    ds18b20_temperature = get_temperature_from_ds18b20()
    _, dht11_humidity = read_from_DHT11().values()
    if ds18b20_temperature is not None and dht11_humidity is not None:
        return jsonify(
            {
                "temperature": ds18b20_temperature,
                "humidity": dht11_humidity
            }
        )
