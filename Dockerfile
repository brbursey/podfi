FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

ENV FLASK_APP=app.py

RUN apt -y update && apt install -y ffmpeg

CMD flask run -h 0.0.0 -p 3000