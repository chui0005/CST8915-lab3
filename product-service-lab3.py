from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env if available

load_dotenv()

app = Flask(__name__)

# Configure CORS: allow any origin, restrict to GET requests

CORS(app) # resources={r"/products": {"origins": "*"}}, methods=["GET"]

# Static product data (equivalent to Rust's vec![])

PRODUCTS = [
  {"id": 1, "name": "Dog Food", "price": 19.99},
  {"id": 2, "name": "Cat Food", "price": 34.99},
  {"id": 3, "name": "Bird Seeds", "price": 10.99},
]

@app.route("/products", methods=["GET"])
def get_products():
  return jsonify(PRODUCTS)

if __name__ == "__main__":
  # Get port from environment or default to 3030
  port = int(os.getenv("PORT", "3030"))
  # Run Flask server (host=0.0.0.0 to match Rust's binding)
  app.run(host="0.0.0.0", port=port)
