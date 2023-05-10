from pymongo import MongoClient
from bson import ObjectId


class ProductsDB:
    def __init__(self):
        self.__client = MongoClient("localhost", 27017)
        self.__db = self.__client["StoreDB"]
        self.__collection = self.__db["Products"]

    def get_all_products(self):
        products = list(self.__collection.find({}))
        return products

    def get_one_product(self, id):
        product = self.__collection.find_one({"id": id})
        return product

    def update_product(self, id, obj):
        self.__collection.update_one({"id": id}, {"$set": obj})

    def delete_product(self, id):
        self.__collection.delete_one({"id": id})
