from fastapi import FastAPI, Form
from pydantic import BaseModel
import io
import sys

app = FastAPI()

# Function to capture terminal output
def capture_output(func):
    buffer = io.StringIO()
    sys.stdout = buffer
    func()
    sys.stdout = sys.__stdout__
    return buffer.getvalue()

# Data model for form submission
class FormData(BaseModel):
    sequence_name: str
    dataset_name: str
    image_H: int
    image_w: int

@app.post("/submit")
async def submit_form(
    sequence_name: str = Form(...),
    dataset_name: str = Form(...),
    image_H: int = Form(...),
    image_w: int = Form(...)
):
    def generate_output():
        print(f"Sequence Name: {sequence_name}")
        print(f"Dataset Name: {dataset_name}")
        print(f"Image Height: {image_H}")
        print(f"Image Width: {image_w}")

    output = capture_output(generate_output)
    return {"output": output}
