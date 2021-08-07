from flask import Flask
from config import config_options

def createApp(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    return app