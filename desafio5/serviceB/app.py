from flask import Flask
import requests

app = Flask(__name__)

@app.route("/info")
def info():
    response = requests.get("http://servicea:5000/users")
    users = response.json()
    result = [f"Usuário {u['nome']} ativo desde {u['ativo_desde']}" for u in users]
    return {"informacoes": result}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
