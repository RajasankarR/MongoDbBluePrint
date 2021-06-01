from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo


f_app=Flask(__name__)
f_app.config.from_object(Config)
mongo=PyMongo(f_app)

from app import routes,models