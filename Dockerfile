FROM python:3.10-slim
WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["bash", "-c", "sleep 5 && python core/engine.py && uvicorn api.server:app --host 0.0.0.0 --port 8000"]
