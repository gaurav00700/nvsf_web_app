# Use an official Python runtime as a parent image
FROM python:3.9-slim

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

# Expose the port to run FastAPI and Streamlit
EXPOSE 8501

# Define the command to run Streamlit
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]