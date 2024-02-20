# Using Ubuntu as an example
FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive

RUN apt update && apt install -y tcl


# Install Python 3.11 (update if the method has changed)
RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y python3.11 python3.11-venv

# Rest of your Dockerfile instructions as before... 
FROM python:3.11-bullseye

# Set working directory 
WORKDIR /app

# Copy all app files
COPY . /app 

# Install dependencies
RUN pip install -r requirements.txt

# Expose container port (usually 8080)
EXPOSE 8080

# Command to start the Flask app
CMD ["gunicorn", "-b", ":8080", "main:app"] 
