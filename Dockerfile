# Use a lightweight Python Linux setup
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy files from your machine to the container
COPY..

# Install dependencies
RUN pip install -r requirements.txt

# Run the web server (Gunicorn)
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
