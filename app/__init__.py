from flask import Flask
from .config import config
from .utils.log import Log
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .module import Modules


db = SQLAlchemy()
cors = CORS()
def create_app(env='production'):
    app = Flask(__name__)
    app.config.from_object(config[env])
    db.init_app(app)
    cors.init_app(app)
    Log(app, as_email=False, as_sentry=True)
    Modules(app)
    return app