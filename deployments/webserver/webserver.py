from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Here you shall upload your image and text"


@app.route("/ready")
def ready():
    return "", 200
