# Stage 1: Build stage
FROM python:3.12-slim as build

# Install Git and other dependencies
RUN apt-get update && apt-get install -y git

# Set the working directory in the container
WORKDIR /app

# Copy the entire context to the container
COPY . .

# Get the current Git branch and build time
RUN echo $(date +'%Y%m%d-%H%M%S') > /app/BUILT_AT

# Stage 2: Production stage
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /opt/mentorhub-COLLECTION-api

# Copy the entire source code and the BUILT_AT file from the build stage
COPY --from=build /app/ /opt/mentorhub-COLLECTION-api/

# Install pipenv and dependencies
COPY Pipfile Pipfile.lock /opt/mentorhub-COLLECTION-api/
RUN pip install pipenv && pipenv install --deploy --system

# Install Gunicorn for running the Flask app in production
RUN pip install gunicorn gevent

# Expose the port the app will run on
EXPOSE 8088

# Set Environment Variables
ENV PYTHONPATH=/opt/mentorhub-COLLECTION-api

# Command to run the application using Gunicorn with exec to forward signals
CMD exec gunicorn --bind 0.0.0.0:8088 src.server:app
