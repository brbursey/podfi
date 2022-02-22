import os
from flask import Flask
from flask import request
from main import merge

app = Flask(__name__)

@app.route("/test")
def hello():
    merge()
    return "Hello World!"