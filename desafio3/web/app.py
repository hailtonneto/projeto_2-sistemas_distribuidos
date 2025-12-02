from flask import Flask
import psycopg2
import redis
import os

app = Flask(__name__)

db_host = os.getenv("DB_HOST", "db")
db_name = os.getenv("DB_NAME", "mydb")
db_user = os.getenv("DB_USER", "user")
db_password = os.getenv("DB_PASSWORD", "password")

cache_host = os.getenv("CACHE_HOST", "cache")
r = redis.Redis(host=cache_host, port=6379)

@app.route("/")
def index():
    visits = r.incr("visits")

    conn = psycopg2.connect(host=db_host, dbname=db_name, user=db_user, password=db_password)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS usuarios (id SERIAL PRIMARY KEY, nome VARCHAR(50));")
    conn.commit()
    cur.close()
    conn.close()

    return f"Visita número {visits} - Banco conectado com sucesso!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
