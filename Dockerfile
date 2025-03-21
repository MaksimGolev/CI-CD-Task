FROM python:3.11-slim

RUN adduser --disabled-password --gecos '' myuser

USER myuser

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
