import os
import streamlit as st
import requests

# Get the FastAPI URL from environment variable
fastapi_url = os.getenv('FASTAPI_URL', 'http://fastapi:8000')  # Use the Docker service name

st.title('Synthetic Data Details')

sequence_name = st.text_input('Sequence Name (String):')
dataset_name = st.text_input('Dataset Name (String):')
image_H = st.number_input('Image Height (Integer):', min_value=1, max_value=10000, step=1)
image_w = st.number_input('Image Width (Integer):', min_value=1, max_value=10000, step=1)

if st.button('Submit'):
    try:
        response = requests.post(f"{fastapi_url}/submit", json={
            'sequence_name': sequence_name,
            'dataset_name': dataset_name,
            'image_H': image_H,
            'image_w': image_w
        })
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        st.text_area("Terminal Output:", data.get("output", ""), height=300)
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
