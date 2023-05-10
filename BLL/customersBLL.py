from DAL.customers_DAL import CustomersDB


class CustomersBLL:
    def __init__(self):
        self.__products = CustomersDB()

    def get_all_customers(self):
        customers = []
        customers_data = self.__products.get_all_customers()

        for c in customers_data:

            obj = {
                "id": c["id"],
                "fName": c["First_Name"],
                "lName": c["Last_Name"],
                "city": c["City"],
            }

            customers.append(obj)
        return customers

    def get_one_customer(self, id):
        customer_data = self.__products.get_one_customer(id)
        print(customer_data)

        obj = {
            "fName": customer_data["First_Name"],
            "lName": customer_data["Last_Name"],
            "city": customer_data["City"],
        }
        return obj

    def update_customer(self, id, obj):
        obj = {
            "First_Name": obj["fName"],
            "Last_Name": obj["lName"],
            "City": obj["city"],
        }
        self.__products.update_customer(id, obj)
        return "Updated!"

    def delete_customer(self, id):
        self.__products.delete_customer(id)
        return "Deleted!"
