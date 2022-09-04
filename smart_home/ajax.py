
from smart_home.sensors.DS18b20 import get_temperature_from_ds18b20
from smart_home.sensors.DHT11 import read_from_DHT11
from flask import jsonify
from smart_home import app

# For Ajax
@app.route("/refresh_data", methods=['GET'])
def refresh_data():
    ds18b20_temperature = get_temperature_from_ds18b20()
    _, dht11_humidity = read_from_DHT11().values()
    return jsonify(
        {
            "temperature": ds18b20_temperature,
            "humidity": dht11_humidity
        }
    )
