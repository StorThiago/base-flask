# FROM python:3.9

# WORKDIR /app

# COPY requirements.txt requirements.txt

# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "wsgi:app"]


## PRODUCTION
FROM python:3.9-slim

WORKDIR /app

# Primeiro copia apenas o requirements.txt para aproveitar cache de camadas
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Depois copia o resto dos arquivos
COPY . .

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:$PORT"]