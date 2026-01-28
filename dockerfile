FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /root/.streamlit
COPY .streamlit/config.toml /root/.streamlit/config.toml

EXPOSE 8000
EXPOSE 8501

CMD ["sh", "-c", "\
uvicorn src.app:app --host 0.0.0.0 --port 8000 & \
streamlit run frontend/app.py --server.port 8501 --server.address 0.0.0.0 \
"]
