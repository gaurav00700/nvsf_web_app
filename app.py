import streamlit as st
import requests

st.title('Synthetic Data Details')

with st.form(key='data_form'):
    sequence_name = st.text_input('Sequence Name (String):')
    dataset_name = st.text_input('Dataset Name (String):')
    image_H = st.number_input('Image Height (Integer):', min_value=1, max_value=10000, step=1)
    image_w = st.number_input('Image Width (Integer):', min_value=1, max_value=10000, step=1)
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    # Send the data to the FastAPI backend
    response = requests.post("http://127.0.0.1:8000/submit", data={
        "sequence_name": sequence_name,
        "dataset_name": dataset_name,
        "image_H": image_H,
        "image_w": image_w
    })
    data = response.json()
    st.text_area("Terminal Output:", data.get("output", ""), height=300)
