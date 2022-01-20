from flask import Flask
from flask_pymongo import PyMongo

from commands.import_amz_data import commands
from config import Config
from graphqls.routes import graphql_routes

MONGO_HOST = Config.MONGO_HOST
MONGO_PORT = Config.MONGO_PORT
MONGO_DB = Config.MONGO_DB_NAME

app = Flask(__name__)
# Config mongodb in to the app
app.config["MONGO_URI"] = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"  # NOQA
mongodb_client = PyMongo(app)
db = mongodb_client.db

app.register_blueprint(commands)
app.register_blueprint(graphql_routes)
