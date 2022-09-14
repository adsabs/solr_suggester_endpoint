FROM python:3.8

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -ms /bin/bash ads