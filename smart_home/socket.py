from glob import glob
import imp
from smart_home import app, socketio
from threading import Lock
from smart_home.sensors.DS18b20 import get_temperature_from_ds18b20
from smart_home.sensors.DHT11 import read_from_DHT11
from .config import SENSOR_TEMP_HUM_REFRESH_TIME

thread = None
async_mode = None
thread_lock = Lock()

namespace = '/sensor_temperature'

@socketio.on('connect', namespace=namespace)
def connect():
    print('Client connected!')
    def read_sensor_thread():
        while True:
            socketio.sleep(SENSOR_TEMP_HUM_REFRESH_TIME)
            temperature = get_temperature_from_ds18b20()
            _, humidity = read_from_DHT11().values()

            if temperature is not None and humidity is not None:
                socketio.emit('server_response_sensor_temperature', 
                {'temperature': temperature, 'humidity': humidity}, 
                namespace=namespace)
                print('SockerIO server send: Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))

    global thread
    with thread_lock:
        if not thread:
            socketio.start_background_task(target=read_sensor_thread)
    

@socketio.on('disconnect', namespace=namespace)
def disconnect():
    print('Client disconnected!')
