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
    DATABASE = {
        'USERNAME': 'sensor_dev', // this username will be the username for your central logging server
        'PASSWORD': 'mcsc',       // this password will be the password for your central logging server
        'HOST': '192.168.56.101', // this I.P. will match the I.P. of the central logging server
        'DB_NAME': 'sensor'       // this is the name of your central logging server 
    }
___
