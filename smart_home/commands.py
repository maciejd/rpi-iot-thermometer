import click
import time
import datetime
from smart_home import app
from smart_home import db
from smart_home.models import TempHumidityData
import smart_home.sensors.DHT11 as DHT11
import smart_home.sensors.DS18b20 as DS18b20


@app.cli.command()
@click.option('--drop', is_flag=True)
def initdb(drop: bool):
    """init the database"""
    if drop:
        click.confirm('This will delete the database, continue ?', abort=True)
        db.drop_all()
        click.echo('Drop tables')
    db.create_all()
    click.echo('Inited databse')


@app.cli.command()
def forge():
    db.drop_all()
    db.create_all()

    while True:
        time.sleep(5)
        temperature = DS18b20.get_temperature_from_ds18b20()
        _, humidity = DHT11.read_from_DHT11().values()
        timestamp = datetime.datetime.utcnow()
        if temperature is not None and humidity is not None:
            sensor_data = TempHumidityData.add(temp=temperature, humidity=humidity, timestamp=timestamp)
            print(sensor_data)

