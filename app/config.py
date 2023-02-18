import os
from dotenv import load_dotenv

path = os.path.join(os.path.dirname(__file__), '../.env')
if os.path.exists(path):
    load_dotenv(path)
else:
    print('Error: ENV NOT FOUND')
    exit


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', default='sqlite:///:memory:')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS',default=True)


class Development(Config):
    DEBUG=True


class Production(Config):
    DEBUG=False


config = {
    'development' : Development,
    'production' : Production,
}