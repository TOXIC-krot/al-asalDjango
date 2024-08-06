FROM python:3.12-slim-bullseye

WORKDIR /usr/src/app

# Set environment variables to ensure Python runs in a consistent environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install gcc and other necessary build tools
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Set up environment variables for the application
ENV HOME=/home/app
ENV APP_HOME=/home/app/web

# Create necessary directories for the application
RUN mkdir -p $HOME
RUN mkdir $APP_HOME

# Set the working directory for the application
WORKDIR $APP_HOME

# Copy the application code into the container
COPY . .

# Specify the entry point for the container
ENTRYPOINT ["python", "main.py"]
