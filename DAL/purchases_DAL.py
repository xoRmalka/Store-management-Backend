from pymongo import MongoClient
from bson import ObjectId


class PurchasesDB:
    def __init__(self):
        self.__client = MongoClient("localhost", 27017)
        self.__db = self.__client["StoreDB"]
        self.__collection = self.__db["Purchases"]

    def get_all_purchases(self):
        purchases = list(self.__collection.find({}))
        return purchases

    def get_one_purchase(self, id):
        customer = self.__collection.find_one({"id": id})
        return customer

    def delete_purchase(self, id):
        self.__collection.delete_one({"id": id})
        return "Deleted!"

    def create_purchase(self, obj):
        self.__collection.insert_one(obj)
        return "Purchase Created!"
