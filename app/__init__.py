from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def register_extensions(app):
    """Intialize extensions with app
    Args:
        app (Flask): Flask app instance
    """
    db.init_app(app)


def create_db(app):
    with app.app_context():
        db.create_all()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    register_extensions(app)
    create_db(app)

    return app
