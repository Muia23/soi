import os

class Config:
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://willy:willy@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'secret'

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    pass


class DevConfig(Config):
    
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}