from flask import Flask
from config import config_options


def create_app(config_name):
    
    #Initialize the app
    app = Flask(__name__)    

    

    return app