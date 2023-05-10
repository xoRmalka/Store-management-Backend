from flask import Blueprint, jsonify, request

from BLL.purchasesBLL import PurchasesBLL

purchases = Blueprint("purchases", __name__)
purchases_bll = PurchasesBLL()


@purchases.route("/", methods=["GET"])
def get_all_purchases():
    args = request.args
    customerId = args.get('customerId')
    purchases = purchases_bll.get_all_purchases()

    if customerId is None:
        return jsonify(purchases)
    elif customerId is not None:
        fil = []
        for p in purchases:
            print(p)
            if p["customerId"] == customerId:
                fil.append(p)
        return jsonify(fil)


@purchases.route("<int:id>", methods=["DELETE"])
def delete_purchase(id):
    status = purchases_bll.delete_purchase(id)
    return jsonify(status)


@purchases.route("/", methods=["POST"])
def create_purchase():
    obj = request.json
    status = purchases_bll.create_purchase(obj)
    return jsonify(status)
