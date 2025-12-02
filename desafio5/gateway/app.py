from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "API Gateway rodando! Endpoints: /users e /info"

@app.route("/users")
def users():
    response = requests.get("http://servicea:5000/users")
    return jsonify(response.json())

@app.route("/info")
def info():
    response = requests.get("http://serviceb:6000/info")
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
