# Defines the baseline image, in this case python:3.8-slim, we want to use to create our own Docker image
FROM python:3.8

# WORKDIR <name-of-working-directory-in-container> - Defines the home directory of your container
WORKDIR /app

# Copy requirements file from the directory the Docker file is in into the /app directory of the container
COPY requirements.txt /app

# Executes pip install command and installs all required python libraries
RUN pip install --trusted-host pypi.python.org -r requirements.txt

ADD . /app

# Run this file: tweet_collector.py
CMD ["python", "etl.py"]