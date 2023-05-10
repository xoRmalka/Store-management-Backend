from DAL.purchases_DAL import PurchasesDB


class PurchasesBLL:
    def __init__(self):
        self.__purchases = PurchasesDB()

    def get_all_purchases(self):
        purchases = []
        purchases_data = self.__purchases.get_all_purchases()

        for p in purchases_data:

            obj = {
                "id": p["id"],
                "customerId": p["CustomerID"],
                "productId": p["ProductID"],
                "date": p["Date"],
            }

            purchases.append(obj)
        return purchases

    def delete_purchase(self, id):
        self.__purchases.delete_purchase(id)

    def create_purchase(self, obj):
        purchase = {
            "id": obj["id"],
            "CustomerID": obj["customerId"],
            "ProductID": obj["productId"],
            "Date": obj["date"],
        }
        self.__purchases.create_purchase(purchase)
