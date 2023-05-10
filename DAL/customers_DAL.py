from pymongo import MongoClient
from bson import ObjectId


class CustomersDB:
    def __init__(self):
        self.__client = MongoClient("localhost", 27017)
        self.__db = self.__client["StoreDB"]
        self.__collection = self.__db["Customers"]

    def get_all_customers(self):
        customers = list(self.__collection.find({}))
        return customers

    def get_one_customer(self, id):
        customer = self.__collection.find_one({"id": id})
        return customer

    def update_customer(self, id, obj):
        self.__collection.update_one({"id": id}, {"$set": obj})

    def delete_customer(self, id):
        self.__collection.delete_one({"id": id})
