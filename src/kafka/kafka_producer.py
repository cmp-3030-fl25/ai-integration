from confluent_kafka import Producer
import json
import time

conf = {
    "bootstrap.servers": "localhost:9092"
}

producer = Producer(conf)

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def send_message(topic, data):
    payload = json.dumps(data).encode("utf-8")
    producer.produce(topic, value=payload, callback=delivery_report)
    producer.poll(0)  # Trigger callbacks

if __name__ == "__main__":
    for i in range(5):
        event = {"user_id": i, "action": "click", "ts": time.time()}
        send_message("events", event)
        time.sleep(1)

    producer.flush()
