import os
import streamlit as st
import requests

# Get the FastAPI URL from environment variable
fastapi_url = os.getenv('FASTAPI_URL', 'http://fastapi:8000')  # Use the Docker service name

st.title('Synthetic Data Details')

dataset_name = st.text_input('Dataset Name (String):')
sequence_name = st.text_input('Sequence Name ("daas", "dgt", "kitti360"):')
delta_pos_lidar = st.text_input('Delta Lidar position ([0.0, 0.0, 0.0]):')
delta_orient_lidar = st.text_input('Delta Lidar orientation ([0.0, 0.0, 0.0]):')
intrinsics_lidar_new = st.text_input('Lidar vertical fov ([up_fov(float), fov(float)]):')
intrinsics_hoz_lidar_new = st.text_input('Lidar horizontal fov ([up_fov(float), fov(float)]):')
V_lidar_ch = st.text_input('Lidar vertical beams (int):')
H_lidar_ch = st.text_input('Lidar horizontal beams (int):')
Lidar_range = st.text_input('Lidar maximum range in m (float):')
delta_pos_cam = st.text_input('Delta camera position ([0.0, 0.0, 0.0]):')
delta_orient_cam = st.text_input('Delta camera orientation ([0.0, 0.0, 0.0]):')
image_H = st.number_input('Image Height (Integer):', min_value=500, max_value=5000, step=1)
image_W = st.number_input('Image Width (Integer):', min_value=500, max_value=5000, step=1)

if st.button('Submit'):
    try:
        response = requests.post(f"{fastapi_url}/submit", json={
            'dataset_name': dataset_name,
            'sequence_name': sequence_name,
            'delta_pos_lidar': delta_pos_lidar,
            'delta_orient_lidar': delta_orient_lidar,
            'intrinsics_lidar_new': intrinsics_lidar_new,
            'intrinsics_hoz_lidar_new': intrinsics_hoz_lidar_new,
            'V_lidar_ch': V_lidar_ch,
            'H_lidar_ch': H_lidar_ch,
            'Lidar_range': Lidar_range,
            'delta_pos_cam': delta_pos_cam,
            'delta_orient_cam': delta_orient_cam,
            'image_H': image_H,
            'image_W': image_W
        })
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        st.text_area("Terminal Output:", data.get("output", ""), height=300)
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
