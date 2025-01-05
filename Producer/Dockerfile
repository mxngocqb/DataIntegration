# Step 1: Use an official Python image from the Docker Hub
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy your Python script into the container
COPY producer.py /app/producer.py

# Step 4: Install any necessary dependencies
RUN pip install confluent_kafka

# Step 5: Set environment variables (optional but useful for Kafka connections)
# ENV KAFKA_BROKER='kaf1:9092,kaf2:9093'

# Step 6: Define the command to run your script when the container starts
CMD ["python", "producer.py"]
