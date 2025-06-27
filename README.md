# 🕒 SimpleTimeService

A minimalist FastAPI-based web service that returns the current server time.

## Features

- Lightweight and fast
- Returns current server time in ISO format
- Dockerized for easy deployment

## ▶ Running 

### 1. Clone the repo

```bash
git clone https://github.com/gnk0504/simpletimeservice.git
cd simpletimeservice

# Build Docker image
docker build -t simple-time-service .

# Run the container (map to port 80)
docker run -d -p 80:8000 simple-time-service

Test It

In your browser:
http://<your-ec2-public-ip>/

http://<your-ec2-public-ip>/time
