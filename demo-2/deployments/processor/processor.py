from datetime import datetime 
from google.cloud import pubsub_v1, storage
from uuid import uuid4

subscriber_client = pubsub_v1.SubscriberClient()
subscription_path = subscriber_client.subscription_path("lorenzo-scratch-space", "processor")

storage_client = storage.Client()
storage_client.bucket("cc-demo-lorenzo-feedback")


def process_message(message):
    print(f"Received message: {message}")

    timestamp = datetime.utcnow().isoformat()
    random_append = uuid4().hex

    blob = bucket.blob(f"{timestamp}-{random_append}")
    blob.upload_from_string(message)

    message.ack()


streaming_pull_future = subscriber_client.subscribe(subscription_path, callback=process_message)

print(f"Listening for messages on {subscription_path}..")

try:
    streaming_pull_future.result()
except:
    streaming_pull_future.cancel()