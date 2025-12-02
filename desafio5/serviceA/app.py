from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users")
def users():
    data = [
        {"id": 1, "nome": "Hailton", "ativo_desde": "2023"},
        {"id": 2, "nome": "Maria", "ativo_desde": "2024"}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
