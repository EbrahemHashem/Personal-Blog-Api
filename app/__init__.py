from app.extensions import migrate
from flask import Flask
from app.extensions import bcrypt, cors, jwt, ma
from config import config_by_name
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    register_extensions(app)
    from .api import api_bp
    # Register blueprints
    app.register_blueprint(api_bp, url_prefix="/")

    return app


def register_extensions(app):
    # Registers flask extensions
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)