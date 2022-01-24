from smart_home import app
import os

# 设置数据库的路径
dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'sensor_data.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
