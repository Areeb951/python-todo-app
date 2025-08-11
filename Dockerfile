# Use a lightweight Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies (including pytest)
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir pytest

# Copy application files
COPY . .

# Expose the port your app runs on
EXPOSE 8000

# Run the application
CMD ["python", "app.py"]
