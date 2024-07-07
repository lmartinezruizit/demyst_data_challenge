# Use an appropriate base image with Python 3.9
FROM openjdk:8-jdk-slim

# Install Python 3.9 and pip
RUN apt-get update && \
    apt-get install -y python3.9 python3.9-dev python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install PySpark 3.1.2
RUN pip3 install pyspark==3.1.2

# Set Python 3.9 as the default python
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1

# Set the working directory
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Set environment variables for PySpark
ENV PYSPARK_PYTHON=python3.9
ENV PYSPARK_DRIVER_PYTHON=python3.9

# Specify the command to run
CMD ["spark-submit", "--conf", "spark.driver.extraJavaOptions=--add-opens=java.base/java.nio=ALL-UNNAMED", "--conf", "spark.executor.extraJavaOptions=--add-opens=java.base/java.nio=ALL-UNNAMED", "/app/data_processing/minimal.py"]
