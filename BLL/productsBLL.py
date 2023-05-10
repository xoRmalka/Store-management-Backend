from DAL.products_DAL import ProductsDB


class ProductsBLL:
    def __init__(self):
        self.__products = ProductsDB()

    def get_all_products(self):
        products = []
        products_data = self.__products.get_all_products()

        for p in products_data:

            obj = {
                "id": p["id"],
                "name": p["Name"],
                "price": p["Price"],
                "quantity": p["Quantity"],
            }

            products.append(obj)
        return products

    def get_one_product(self, id):
        product_data = self.__products.get_one_product(id)
        print(product_data)

        obj = {
            "id": product_data["id"],
            "name": product_data["Name"],
            "price": product_data["Price"],
            "quantity": product_data["Quantity"],
        }
        return obj

    def update_product(self, id, obj):
        obj = {
            "Name": obj["name"],
            "Price": obj["price"],
            "Quantity": obj["quantity"],
        }
        self.__products.update_product(id, obj)
        return "Updated!"

    def delete_product(self, id):
        self.__products.delete_product(id)
        return "Deleted!"
