# 1. Use the lightweight official Python image
FROM python:3.13-alpine

# 2. Set a working directory
WORKDIR /app

# 3. Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the application code
COPY app.py .

# 5. Expose the port
EXPOSE 5000

# 6. Default command
CMD ["python", "app.py"]
