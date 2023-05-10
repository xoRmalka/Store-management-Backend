from flask import Flask
from flask_cors import CORS


from Routers.purchases_router import purchases
from Routers.products_router import products
from Routers.customers_router import customers


app = Flask(__name__)

CORS(app)

app.register_blueprint(purchases, url_prefix="/purchases")
app.register_blueprint(products, url_prefix="/products")
app.register_blueprint(customers, url_prefix="/customers")


app.run()
