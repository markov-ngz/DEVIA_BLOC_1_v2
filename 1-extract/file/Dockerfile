FROM python:3.11-slim

# Install Java (required for PySpark)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    default-jdk \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PYTHONPATH=/app/src
ENV PYSPARK_PYTHON=python3

# Create and set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY ./src/ src/

# Set the default command
CMD ["python", "src/main.py"]