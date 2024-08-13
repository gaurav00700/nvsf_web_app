from fastapi import FastAPI
from pydantic import BaseModel
import io
import sys

app = FastAPI()

class Data(BaseModel):
    sequence_name: str
    dataset_name: str
    image_H: int
    image_w: int

# Function to capture terminal output
def capture_output(func, *args, **kwargs):
    buffer = io.StringIO()
    sys.stdout = buffer
    func(*args, **kwargs)
    sys.stdout = sys.__stdout__
    return buffer.getvalue()

def generate_output(data: Data):
    print(f"Sequence Name: {data.sequence_name}")
    print(f"Dataset Name: {data.dataset_name}")
    print(f"Image Height: {data.image_H}")
    print(f"Image Width: {data.image_w}")

@app.post("/submit")
def submit_data(data):
    output = capture_output(generate_output(data))
    return {"output": output}
