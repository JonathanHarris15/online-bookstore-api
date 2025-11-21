from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from .config import DevelopmentConfig

db = SQLAlchemy() 
api = Api()

def create_app(config_class=DevelopmentConfig):
    """
    Application Factory function. Creates and configures the Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(config_class) # Loads configuration from app/config.py

    # 1. Initialize Extensions with the app instance
    db.init_app(app) # Links the SQLAlchemy object to the running app and its config
    api.init_app(app) # Links the Flask-RESTful object
    
    return app