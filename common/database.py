
import os
import pymongo


class Database(object):
    #URI = os.environ.get("MONGOLAB_URI")
    #DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient("mongodb://Test:Test123@ds259528.mlab.com:59528/heroku_zptt3q6d")
        Database.DATABASE = client.get_default_database()

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
