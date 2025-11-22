from confluent_kafka import Consumer, KafkaException
import json

conf = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "my_python_group_2",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(conf)
consumer.subscribe(["events"])

try:
    while True:
        msg = consumer.poll(1.0)  # Wait for message up to 1 second

        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())

        data = json.loads(msg.value().decode("utf-8"))
        print(f"Received: {data}")

except KeyboardInterrupt:
    print("Stopping consumer...")

finally:
    consumer.close()
