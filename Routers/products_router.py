from flask import Blueprint, jsonify, request

from BLL.productsBLL import ProductsBLL

products = Blueprint("products", __name__)
products_bll = ProductsBLL()


@products.route("/", methods=["GET"])
def get_all_products():
    products = products_bll.get_all_products()
    return jsonify(products)


@products.route("<int:id>", methods=["GET"])
def get__product(id):
    product = products_bll.get_one_product(id)
    return jsonify(product)


@products.route("<int:id>", methods=["PUT"])
def update_product(id):
    obj = request.json
    status = products_bll.update_product(id, obj)
    return jsonify(status)


@products.route("<int:id>", methods=["DELETE"])
def delete_student(id):
    status = products_bll.delete_product(id)
    return jsonify(status)
