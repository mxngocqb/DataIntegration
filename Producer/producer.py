import json
from confluent_kafka import Producer

# Define the delivery report callback
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Kafka configuration
producer_config = {
    'bootstrap.servers': 'kaf1:9092',  # Specify multiple brokers
    'client.id': 'python-producer'
}

# Create the producer instance
producer = Producer(producer_config)

# Send JSON messages
try:
    for i in range(30):
        message = {
            "message": f"Hello Kafka! Message {i}",
            "index": i
        }
        producer.produce(
            topic='test-topic',  # Replace with your topic name
            key=str(i),
            value=json.dumps(message),  # Convert the dictionary to a JSON string
            callback=delivery_report
        )
        producer.flush()  # Ensure delivery of each message (can also batch for performance)

except KeyboardInterrupt:
    print("\nProducer stopped.")

finally:
    producer.flush()  # Ensure all messages are delivered before exiting
