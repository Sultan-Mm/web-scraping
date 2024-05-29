# official Python runtime as a parent image
FROM python:3.11-slim

# Working directory in the container
WORKDIR /app

# Copy only requirements file first for caching
COPY requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Define the command to run your Scrapy spider
CMD ["scrapy", "crawl", "louiserardspider", "-o", "/app/output/New_Output3.json"]





