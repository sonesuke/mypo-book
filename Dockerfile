FROM python:3.7.10-slim-buster

RUN apt update && \
    apt install -y make && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install sphinx pydata-sphinx-theme