import sys
import Adafruit_DHT
import json

SENSOR_MAP = {
    'DHT11': Adafruit_DHT.DHT11,
    'DHT22': Adafruit_DHT.DHT22,
    'AM2302': Adafruit_DHT.AM2302
}

def main():
    sensor_config = {
        "sensor_type": "DHT11",
        "sensor_name": "raspberry_3b_plus_DHT11",
        "pin_id": 16
    }
    sensor_type = sensor_config['sensor_type']
    sensor_name = sensor_config['sensor_name']
    sensor_pin_id = sensor_config['pin_id']
    print('*'*50)
    print('Sensor Type: {}'.format(sensor_type))
    print('Sensor Name: {}'.format(sensor_name))
    print('Sensor PIN: {}'.format(sensor_pin_id))
    print('*'*50)

    assert sensor_type in ['DHT11', 'DHT22', 'AM2302']
    sensor = SENSOR_MAP[sensor_type]
    # Read data
    humidity, temperature = Adafruit_DHT.read(sensor=sensor, pin=sensor_pin_id)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)


def read_from_DHT11():
    sensor_config = {
        "sensor_type": "DHT11",
        "sensor_name": "raspberry_3b_plus_DHT11",
        "pin_id": 16
    }
    sensor_type = sensor_config['sensor_type']
    sensor_name = sensor_config['sensor_name']
    sensor_pin_id = sensor_config['pin_id']
    assert sensor_type in ['DHT11', 'DHT22', 'AM2302']
    sensor = SENSOR_MAP[sensor_type]
    # Read data
    humidity, temperature = Adafruit_DHT.read(sensor=sensor, pin=sensor_pin_id)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        pass
        # print('Failed to get reading. Try again!')
        # sys.exit(1)
    return {'temperature': temperature, 'humidity': humidity}


if __name__ == '__main__':
    # main()
    read_from_DHT11()

# # Parse command line parameters.
# sensor_args = { '11': Adafruit_DHT.DHT11,
#                 '22': Adafruit_DHT.DHT22,
#                 '2302': Adafruit_DHT.AM2302 }
# if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
#     sensor = sensor_args[sys.argv[1]]
#     pin = sys.argv[2]
# else:
#     print('Usage: sudo ./Adafruit_DHT.py [11|22|2302] <GPIO pin number>')
#     print('Example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO pin #4')
#     sys.exit(1)

# # Try to grab a sensor reading.  Use the read_retry method which will retry up
# # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
# humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# # Un-comment the line below to convert the temperature to Fahrenheit.
# # temperature = temperature * 9/5.0 + 32

# # Note that sometimes you won't get a reading and
# # the results will be null (because Linux can't
# # guarantee the timing of calls to read the sensor).
# # If this happens try again!
# if humidity is not None and temperature is not None:
#     print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
# else:
#     print('Failed to get reading. Try again!')
#     sys.exit(1)