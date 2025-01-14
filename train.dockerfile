# Base image
FROM python:3.11-slim AS base

RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*

COPY src/ src/
COPY requirements.txt requirements.txt 
COPY pyproject.toml pyproject.toml

RUN pip install -r requirements.txt
RUN pip install . --no-deps --no-cache-dir --verbose

ENTRYPOINT ["python", "-u", "src/dtu_cnn_classifier/train.py"]