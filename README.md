# FastAPI and Streamlit Application
This repository contains a sample project that includes both a FastAPI backend and a Streamlit frontend. The project demonstrates how to set up and run these services using Docker.

# Project Structure
```
my_project/
│
├── app/
│   ├── api.py          # Streamlit application
│   └── app.py          # FastAPI application
│
├── requirements.txt     # Python dependencies
├── Dockerfile.api_img   # Dockerfile for FastAPI
├── Dockerfile.app_img  # Dockerfile for Streamlit
└── docker-compose.yml   # Docker Compose configuration

```

# Prerequisites
1. Docker
2. Docker Compose

# Setup
1. Build Docker Images for running FastAPI and Streamlit in separate containers:

    ``` 
    docker build -t api_img -f Dockerfile.api .
    docker build -t app_img -f Dockerfile.app .
    ```
2. Run the Containers
    Using Docker Compose
    To manage both containers using Docker Compose, you can use the provided docker-compose.yml file:
    ```
    docker-compose up
    ```
    OR Separate Containers manually
    To run separate containers for FastAPI and Streamlit:
    ```
    docker run -d -p 8000:8000 --name fastapi --network my_network api_img
    docker run -d -p 8501:8501 --name streamlit --network my_network -e FASTAPI_URL=http://fastapi:8000 app_img
    ```
3. Access the Applications 

    * FastAPI: Open `http://localhost:8000` in your web browser to access the FastAPI backend.

    * Streamlit: Open `http://localhost:8501` in your web browser to access the Streamlit frontend.