from smart_home import app
import os


SECRET_KEY = '21328fdsfdasf231fdsf8'

# 设置数据库的路径
dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'sensor_data.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)


# 温度传感器刷新时间
SENSOR_TEMP_HUM_REFRESH_TIME = 10