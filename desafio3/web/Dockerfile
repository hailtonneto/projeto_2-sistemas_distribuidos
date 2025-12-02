FROM python:3.9-slim
WORKDIR /app
COPY app.py .
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*
RUN pip install flask psycopg2 redis
CMD ["python", "app.py"]
