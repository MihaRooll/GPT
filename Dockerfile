FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg libsm6 libxext6 \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["python", "tooncam/manage.py", "runserver", "0.0.0.0:8000"]
