from w1thermsensor import W1ThermSensor
import sqlite3
import threading

def probe():
    threading.Timer(60.0, probe).start()
    conn = sqlite3.connect('temp.db')
    sensor = W1ThermSensor()
    temp = sensor.get_temperature()
    c = conn.cursor()
    c.execute("INSERT INTO temps(temp) VALUES (?)", 
(float(temp),))
    conn.commit()
    conn.close()

probe()
