# Use an official Python runtime as a parent image
FROM python:3.9-slim as base_img

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY app /app

# Stage1: Building api image
FROM base_img as api_img

# Expose the port to run FastAPI
EXPOSE 8000

# Define the command to run the application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]

#Stage2: Building app image
FROM base_img as app_img

# Expose the port to run FastAPI and Streamlit
EXPOSE 8501

# Define the command to run Streamlit
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]