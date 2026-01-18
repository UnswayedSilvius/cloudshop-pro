from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/products")
def products():
    return jsonify([
        {"id": 1, "name": "Laptop", "price": 1200},
        {"id": 2, "name": "Phone", "price": 800}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
