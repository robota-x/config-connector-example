from flask import Flask, render_template, request, redirect, url_for

from google.cloud import pubsub_v1

app = Flask(__name__)

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path("lorenzo-scratch-space", "queued-tweets")


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/send", methods=["POST", "GET"])
def send_ping():
    # no error or success handlers because that's how we roll
    if request.method == "POST":
        tweet_content = request.form.get(
            "tweet-content", "someone tried to post an empty tweet"
        )
        publisher.publish(topic_path, data=tweet_content.encode("utf-8"))
        print(f"publishing tweet! {tweet_content}")

        return redirect(url_for("send_ping"))

    return render_template("sent.html")


@app.route("/ready")
def ready():
    return "", 200
