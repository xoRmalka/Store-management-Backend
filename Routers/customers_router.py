from flask import Blueprint, jsonify, request

from BLL.customersBLL import CustomersBLL

customers = Blueprint("customers", __name__)
customers_bll = CustomersBLL()


@customers.route("/", methods=["GET"])
def get_all_customers():
    customers = customers_bll.get_all_customers()
    return jsonify(customers)


@customers.route("<int:id>", methods=["GET"])
def get_one_customer(id):
    customer = customers_bll.get_one_customer(id)
    return jsonify(customer)


@customers.route("<int:id>", methods=["PUT"])
def update_customer(id):
    obj = request.json
    status = customers_bll.update_customer(id, obj)
    return jsonify(status)


@customers.route("<int:id>", methods=["DELETE"])
def delete_customer(id):
    status = customers_bll.delete_customer(id)
    return jsonify(status)
