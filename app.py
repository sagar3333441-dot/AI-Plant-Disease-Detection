from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import sys
# model folder ko Python path mein add karna
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from model.model import predict_disease

app = Flask(__name__)
CORS(app)


FRONTEND_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "frontend")
)
print("Frontend folder:", FRONTEND_DIR)
print(
    "Index file exists:",
     os.path.exists(os.path.join(FRONTEND_DIR, "index.html"))
     )
@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "login.html")


@app.route("/signup.html")
def signup():
    return send_from_directory(FRONTEND_DIR, "signup.html")  
@app.route("/login.html")
def login():
    return send_from_directory(FRONTEND_DIR, "login.html")
@app.route("/dashboard.html")
def dashboard():
    return send_from_directory(FRONTEND_DIR, "dashboard.html") 
@app.route("/index.html")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html") 
@app.route("/history.html")
def history():
    return send_from_directory(FRONTEND_DIR, "history.html")


@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({
            "error": "No image uploaded"
        }), 400

    image = request.files["image"]

    # AI model se prediction
    result = predict_disease(image)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)