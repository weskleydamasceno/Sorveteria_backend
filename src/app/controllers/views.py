from flask import Flask
from app import app

@app.route("/")
def hello():
    return "Hello!"
