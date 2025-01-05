# Step 1: Use an official Python image from the Docker Hub
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy your Kafka consumer script into the container
COPY consumer.py /app/consumer.py

# Step 4: Install necessary dependencies
RUN pip install kafka-python elasticsearch

# Step 5: Set environment variables for Elasticsearch and Kafka
# Optional: You can set environment variables if necessary (e.g., for easier configuration)
# ENV KAFKA_BROKER='kaf1:9092'
# ENV ELASTICSEARCH_HOST='elasticsearch'
# ENV ELASTICSEARCH_PORT='9200'

# Step 6: Define the command to run your script when the container starts
CMD ["python", "consumer.py"]
