from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()
app=Flask(__name__)
app.config['MONGODB_SETTINGS']={
    'db' :'newdb'
}

db.init__app(app)

from . import views
