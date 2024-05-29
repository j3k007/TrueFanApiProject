# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy project files to the container
COPY . .

# Install dependencies for both APIs
RUN pip install --upgrade pip
RUN pip install -r api/requirements.txt
RUN pip install -r apiForUpdate/requirements.txt
RUN pip install -r apiForDelete/requirements.txt

# Expose the ports for both APIs
EXPOSE 8000 8081 8082

# Start the servers for both APIs
CMD ["sh", "-c", "cd api && python manage.py runserver 0.0.0.0:8000 & cd ../apiForUpdate && python manage.py runserver 0.0.0.0:8081 & cd ../apiForDelete && python manage.py runserver 0.0.0.0:8082"]
