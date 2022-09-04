from smart_home import app
from flask import render_template, jsonify
from smart_home.sensors.DS18b20 import get_temperature_from_ds18b20
from smart_home.sensors.DHT11 import read_from_DHT11


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    temperature = get_temperature_from_ds18b20()
    _, humidity = read_from_DHT11().values()
    # sometime the data are None from sensor
    if not temperature:
        temperature = -1
    if not humidity:
        humidity = -1
    return render_template('home.html', temperature=temperature, humidity=humidity)



