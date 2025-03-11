# FastAPI and Streamlit Application
This repository contains a sample project that includes both a FastAPI backend and a Streamlit frontend. The project demonstrates how to set up and run these services using Docker.

# Prerequisites
1. Docker
2. Docker Compose

# Setup
1. Build Docker Images for running FastAPI and Streamlit in separate containers:
    Using Docker Compose
    ``` 
    docker compose build
    ```

2. Run the Containers
    To manage both containers using Docker Compose, you can use the provided docker-compose.yml file:
    ```
    docker compose up
    ```

3. Access the Applications 

    * Open `http://localhost:8501` in your web browser to access the Streamlit frontend.

# Project Structure
```
my_project/
│
├── app/
│   ├── api.py              # Streamlit application
│   └── app.py              # FastAPI application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Multistage Dockerfile
└── docker-compose.yml      # Docker Compose configuration
```