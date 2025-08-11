# Use Python base image
FROM python:3.10-slim

# Set work directory inside container
WORKDIR /app

# Copy requirements file first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

# Expose app port
EXPOSE 8000

# Command to run the application
CMD ["python", "app.py"]
