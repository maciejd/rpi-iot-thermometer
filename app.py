from flask import Flask, render_template, jsonify
# import sensor
from sensors import DHT11, DS18b20

app = Flask(__name__)

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
