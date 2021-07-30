import logging as log
from .database import Database

bancodados = Database()

def init_app(app):
    print("db_init")
    bancodados.initialize(bancodados, app)
    #database.URI = app.config.get("DB_DATABASE_URI", "mongodb://root:hass123@mongodb:27017")
    #app.config.get("DB_DATABASE_URI", "mongodb://root:hass123@mongodb:27017")

