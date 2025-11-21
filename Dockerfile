# Use a lightweight Python image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first for better caching
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app folder
COPY app/ app/

# Expose port 5000
EXPOSE 5000

# Run the Flask app
CMD ["python", "app/main.py"]
