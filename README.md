# CyberSniffer
Capture cyber attacks as they happen.

___
#### Installation

    git clone https://github.com/maine-cyber/CyberSniffer.git
    cd CyberSniffer
    python setup.py install

___
#### Setup

Change the configs.py to represent your honeypot

    from sqlalchemy.ext.declarative import declarative_base

    BASE = declarative_base()
    SENSOR_IP = '192.168.56.103' // this I.P. will change to match your honeypots I.P. address
    DATABASE = {  // DO NOT CHANGE ANY OF THE DATABASE INFORMATION 
        'USERNAME': 'sensor_dev', 
        'PASSWORD': 'mcsc',       
        'HOST': '192.168.56.101',
        'DB_NAME': 'sensor'       
    }
___
