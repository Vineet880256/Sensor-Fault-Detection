from pymongo import MongoClient
from sensor.configuration.mongo_db_connection import MongoDBClient

if __name__ == '__main__':

    mogodb_client = MongoDBClient()
    print("COllection Name:", mogodb_client.database.list_collection_names())