from app.extensions import migrate, db
from flask import Flask
from app.extensions import bcrypt, cors, jwt, ma
from config import config_by_name
from .api import api_bp


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    register_extensions(app)
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