import os
import json

# with open('/etc/config.json') as config_file:
#     config = json.load(config_file)

# class Config:
#     SECRET_KEY = config.get('SECRET_KEY')
#     SQLALCHEMY_DATABASE_URI = config.get('DATABASE_URI')
#     MAIL_SERVER = 'smtp.googlemail.com'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = config.get('ICT_USER')
#     MAIL_PASSWORD = config.get('ICT_PASS')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('ICT_USER')
    MAIL_PASSWORD = os.environ.get('ICT_PASS')
