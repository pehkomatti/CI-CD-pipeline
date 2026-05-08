# Use a lightweight Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy project files into container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port (Flask app runs on 8080)
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]