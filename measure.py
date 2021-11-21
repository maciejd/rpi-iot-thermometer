# from w1thermsensor import W1ThermSensor
import sqlite3
import threading
import sensor

def probe():
    threading.Timer(0.1, probe).start()
    conn = sqlite3.connect('temp.db')
    # sensor = W1ThermSensor()
    # temp = sensor.get_temperature()
    # temp = 20.5
    temp = sensor.get_temperature_from_ds18b20()
    print('Temp: {} *C'.format(temp))
    c = conn.cursor()
    c.execute("INSERT INTO temps(temp) VALUES (?)", (float(temp),))
    conn.commit()
    conn.close()

probe()
