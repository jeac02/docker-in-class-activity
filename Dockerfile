# Python Flask app container
FROM python:3.12-slim

# Prevent Python from writing .pyc and using buffered stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Workdir
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY app.py /app/

EXPOSE 5000

CMD ["python", "app.py"]
