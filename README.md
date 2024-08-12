# FastAPI and Streamlit Application
This repository contains a sample project that includes both a FastAPI backend and a Streamlit frontend. The project demonstrates how to set up and run these services using Docker.

# Project Structure
```
my_project/
│
├── app/
│   ├── main.py          # Streamlit application
│   └── server.py        # FastAPI application
│
├── requirements.txt     # Python dependencies
├── Dockerfile           # Dockerfile for combined setup
├── Dockerfile.fastapi   # Dockerfile for FastAPI
├── Dockerfile.streamlit # Dockerfile for Streamlit
└── docker-compose.yml   # Docker Compose configuration

```

# Prerequisites
1. Docker
2. Docker Compose (optional, for multi-container setup)

## Setup
1. Build Docker Images
You can choose between building a combined Docker image or separate images for FastAPI and Streamlit.

    ### Combined Docker Image
    If you want to run both services in a single container:
    ```
    docker build -t api_and_app .
    ```

    ### Separate Docker Images
    For running FastAPI and Streamlit in separate containers:

    ``` 
    docker build -t api_img -f Dockerfile.api .
    docker build -t app_img -f Dockerfile.app .
    ```
2. Run the Containers
    Separate Containers
    To run separate containers for FastAPI and Streamlit:
    ```
    docker run -d -p 8000:8000 api_img
    docker run -d -p 8501:8501 app_img
    ```
    OR Using Docker Compose
    To manage both containers using Docker Compose, you can use the provided docker-compose.yml file:
    ```
    docker-compose up
    ```
3. Access the Applications
FastAPI: Open `http://localhost:8000` in your web browser to access the FastAPI backend.
Streamlit: Open `http://localhost:8501` in your web browser to access the Streamlit frontend.