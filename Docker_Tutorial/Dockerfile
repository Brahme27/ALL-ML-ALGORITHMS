# Start with a lightweight Python 3.7 version based on Alpine Linux
FROM python:3.8-alpine

# Copy all files from your current folder into the /app directory inside the container
COPY . /app

# Set the working directory to /app, so all commands below will run from here
WORKDIR /app

# Install the necessary Python packages specified in the requirements.txt file
RUN pip install -r requirements.txt

# Define the command to run when the container starts, which is to run your Python app
CMD python app.py
