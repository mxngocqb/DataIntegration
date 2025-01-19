from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json

# Initialize Elasticsearch client with scheme (http or https) included
es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200, 'scheme': 'http'}])  # Add 'scheme' here

# Kafka consumer configuration
consumer = KafkaConsumer(
    'test-topic',  # Kafka topic to consume from
    bootstrap_servers=['kaf1:9092'],  # List of Kafka broker addresses
)

def push_to_elasticsearch(doc, index='kafka_messages1'):
    """
    Push a document to Elasticsearch.
    """
    try:
        es.index(index=index, body=doc)
        print("Document indexed successfully")
    except Exception as e:
        print(f"Error indexing document: {e}")

try:
    for message in consumer:
        # Decode the message value (assuming it's a UTF-8 string)
        message_value = message.value.decode('utf-8')

        # Assuming the message is JSON, parse it into a Python dict
        try:
            message_json = json.loads(message_value)
        except json.JSONDecodeError:
            print(f"Invalid JSON message: {message_value}")
            continue

        # Push the decoded message to Elasticsearch
        push_to_elasticsearch(message_json)

except KeyboardInterrupt:
    print("Consumer interrupted")

finally:
    # Close the Kafka consumer
    consumer.close()
