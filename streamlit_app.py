import streamlit as st
import io
import sys

# Function to simulate terminal output
def capture_output(func):
    # Create a string buffer to capture output
    buffer = io.StringIO()
    # Redirect stdout to the buffer
    sys.stdout = buffer
    # Run the function
    func()
    # Restore stdout
    sys.stdout = sys.__stdout__
    # Return the content of the buffer
    return buffer.getvalue()

# Set up the title of the web app
st.title('Data Form')

# Create the form
with st.form(key='data_form'):
    sequence_name = st.text_input('Sequence Name (String):')
    dataset_name = st.text_input('Dataset Name (String):')
    image_H = st.number_input('Image Height (Integer):', min_value=1, max_value=10000, step=1)
    image_w = st.number_input('Image Width (Integer):', min_value=1, max_value=10000, step=1)

    # Add a submit button
    submit_button = st.form_submit_button(label='Submit')

# Handle form submission
if submit_button:
    # Define a function to simulate terminal output
    def generate_output():
        print(f"Sequence Name: {sequence_name}")
        print(f"Dataset Name: {dataset_name}")
        print(f"Image Height: {image_H}")
        print(f"Image Width: {image_w}")

    # Capture the terminal output
    output = capture_output(generate_output)
    
    # Display the captured output in the Streamlit app
    st.text_area("Terminal Output:", output, height=300)
