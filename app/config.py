""" App configuration """
import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """ Base config """
    SECRET_KEY = os.getenv('SECRET_KEY', None)
    SERVER_NAME = os.getenv('SERVER_NAME', '127.0.0.1:5000')
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'SQLALCHEMY_DATABASE_URI', f'sqlite:///{os.path.join(BASE_DIR, "db.sqlite3")}')


class DebugConfig(Config):
    """ Development Environment Config """
    DEBUG = True


class ProductionConfig(Config):
    """ Production Environment Config """
    DEBUG = False


config_dict = {
    'debug': DebugConfig,
    'production': ProductionConfig
}
