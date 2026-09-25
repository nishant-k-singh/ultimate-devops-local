from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PRODUCTS = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 55000
    },
    {
        "id": 2,
        "name": "Headphones",
        "price": 2500
    },
    {
        "id": 3,
        "name": "Keyboard",
        "price": 1500
    }
]


@app.route("/")
def home():
    return jsonify({
        "service": "product-service",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/products")
def products():
    return jsonify(PRODUCTS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)