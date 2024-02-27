# Airflow image
FROM apache/airflow:2.8.0

# Copy requirements.txt into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
