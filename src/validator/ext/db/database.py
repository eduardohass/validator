import logging as log
from pymongo import MongoClient

class Database:
    URI = ""#= "mongodb://root:hass123@mongodb:27017"
    DATABASE = ""
    client = None

    # def __init__(self):
    #     log.info("__init__ - database")
        # self.URI = app.config.get("DB_DATABASE_URI")
        # self.DATABASE = app.config.get("DB_DATABASE_NAME")

    @staticmethod
    def initialize(self, app):
        #__import__("ipdb").set_trace()
        log.info("database - initialize")
        log.info("DB_DATABASE_URI="+ str(app.config.get("DB_DATABASE_URI")))
        log.info("DB_DATABASE_NAME="+ str(app.config.get("DB_DATABASE_NAME")))
        self.URI = app.config.get("DB_DATABASE_URI")
        self.DATABASE = app.config.get("DB_DATABASE_NAME")
        client = MongoClient(self.URI)
        self.DATABASE = client[self.DATABASE]

    @staticmethod
    def find(self, collection, query):
        log.info("[database][find]")
        log.info("collection name" - collection)
        return list(self.DATABASE[collection].find(query))
    
    @staticmethod
    def insert(self, collection, data):
        log.info("database - insert")
        self.DATABASE[collection].insert(data)

    @staticmethod
    def find_one(collection, query):
        log.info("[database][find_one]")
        return Database.DATABASE[collection].find_one(query)


    @staticmethod
    def verify_database(database_name):
        log.info("database - verify_database")
        dblist = client.list_database_names()
        print(dblist)
        if database_name in dblist:
            return("The database exists.")  


    @staticmethod
    def verify_collection(collection_name):
        log.info("database - verify_collection")
        collection_list = Database.DATABASE.list_collection_names()
        print(collection_list)
        if collection_name in collection_list:
            return("The collection exists.")
            