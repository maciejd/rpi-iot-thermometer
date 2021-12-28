import time
import random
from app import db, SensorDataHour

def run_sql_hour():
    for i in range(24):
        temperature = random.randint(-20, 35)
        humidity = random.randint(0, 100)
        data = SensorDataHour(temperature=temperature, humidity=humidity, hour=i)
        db.session.add(data)
        db.session.commit()
        print(data)
        time.sleep(3)


if __name__ == '__main__':
    run_sql_hour()


