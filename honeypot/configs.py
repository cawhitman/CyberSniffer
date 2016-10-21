from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()
SENSOR_IP = '192.168.56.103'

DATABASE = {
    'USERNAME': 'sensor_dev',
    'PASSWORD': 'mcsc',
    'HOST': '192.168.56.101',
    'DB_NAME': 'sensor'
}
