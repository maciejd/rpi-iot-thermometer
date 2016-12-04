# rpi-iot-thermometer

Raspberry PI thermometer using DS18B20 sensor with d3.js v4 chart and RESTful API

## Hardware

Connect DS18B20 to RPI using 4.7K resistor as seen on below diagram

![Wiring](https://camo.githubusercontent.com/1419a880b78da3568b1bbf97584490c02ccd5898/68747470733a2f2f63646e2d6c6561726e2e61646166727569742e636f6d2f6173736574732f6173736574732f3030302f3030332f3738322f736d616c6c3336302f6c6561726e5f7261737062657272795f70695f6272656164626f6172642d70726f62652e706e67)


## Software

1. Install W1ThermSensor `pip install w1thermsensor`
2. Install Flask `pip install Flask`
3. Install SQLAlchemy `pip install flask-sqlalchemy`
4. Install SQLite3 `pip install sqlite3`

## Run

1. Initialize database from schema `sqlite3 temp.db < schema.sql`
2. Run probing program in background `nohup python measure.py &`
3. Run flask app
  * `export FLASK_APP=api.py`
  * `flask run --host=0.0.0.0`

## Test

* You should be able to access REST API at `http://127.0.0.1:5000/temp`
```json
{
  "measured_at": "Sat, 03 Dec 2016 14:20:51 GMT", 
  "temperature": 1.5
}
```

* Dashboard should be accessible at http://127.0.0.1:5000/ 
![diagram](https://camo.githubusercontent.com/21aee5aaa0e8bae5f7b7020dbf42a1459690127b/687474703a2f2f692e696d6775722e636f6d2f433345496c6f6d2e706e67)
