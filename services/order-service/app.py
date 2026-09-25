from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

ORDERS = [
    {
        "id": 1,
        "product_id": 1,
        "quantity": 1,
        "status": "confirmed"
    },
    {
        "id": 2,
        "product_id": 2,
        "quantity": 2,
        "status": "pending"
    }
]


@app.route("/")
def home():
    return jsonify({
        "service": "order-service",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/orders", methods=["GET"])
def orders():
    return jsonify(ORDERS)


@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()

    order = {
        "id": len(ORDERS) + 1,
        "product_id": data.get("product_id"),
        "quantity": data.get("quantity", 1),
        "status": "pending"
    }

    ORDERS.append(order)

    return jsonify(order), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)