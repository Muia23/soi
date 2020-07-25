from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()

def create_app(config_name):
    
    #Initialize the app
    app = Flask(__name__)    

    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    #Initialize flask extension
    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)    

    return app