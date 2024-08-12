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
def capture_output(func):
    buffer = io.StringIO()
    sys.stdout = buffer
    func()
    sys.stdout = sys.__stdout__
    return buffer.getvalue()

@app.post("/submit")
def submit_data(data: Data):
    def generate_output():
        print(f"Sequence Name: {data.sequence_name}")
        print(f"Dataset Name: {data.dataset_name}")
        print(f"Image Height: {data.image_H}")
        print(f"Image Width: {data.image_w}")

    output = capture_output(generate_output)
    return {"output": output}
