from flask import Flask
from google.cloud import pubsub_v1

app = Flask(__name__)

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path("lorenzo-scratch-space", "queued-tweets")


@app.route("/")
def hello_world():
    return "Here you shall upload your image and text", 200


@app.route("/send")
def send_ping():
    #  no error or success handlers because that's how we roll
    publisher.publish(topic_path, data="hello test message".encode("utf-8"))

    return "Message sent", 200

@app.route("/ready")
def ready():
    return "", 200
