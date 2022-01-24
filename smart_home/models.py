from datetime import datetime
from smart_home import db

# https://gitee.com/XAUT_975/beibq/blob/master/app/models/model.py
class TempHumidityData(db.Model):
    __tablename = 'temperature_humidity'
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    @staticmethod
    def add(temp, humidity, timestamp):
        data = TempHumidityData()
        data.temperature = temp
        data.humidity = humidity
        data.timestamp = timestamp
        db.session.add(data)
        db.session.commit()
        return data
    
    @staticmethod
    def getbytimestamp(timestamp):
        return TempHumidityData.query.filter_by(timestamp=timestamp).first()
    
    def __str__(self):
        return f'ts:{self.timestamp} tmp:{self.temperature} *C humidity:{self.humidity} %'
