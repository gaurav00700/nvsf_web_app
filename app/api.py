from fastapi import FastAPI
from pydantic import BaseModel
import io
import sys
from typing import List

app = FastAPI()

class Data(BaseModel):
    dataset_name: str
    sequence_name: str
    delta_pos_lidar: List[float]
    delta_orient_lidar: List[float]
    intrinsics_lidar_new: List[float]
    intrinsics_hoz_lidar_new: List[float]
    V_lidar_ch: int
    H_lidar_ch: int
    Lidar_range: float
    delta_pos_cam: List[float]
    delta_orient_cam: List[float]
    image_H: int
    image_W: int

# Function to capture terminal output
def capture_output(func, *args, **kwargs):
    buffer = io.StringIO()
    sys.stdout = buffer
    func(*args, **kwargs)
    sys.stdout = sys.__stdout__
    return buffer.getvalue()

def generate_output(data: Data):
    print(f"Dataset Name: {data.dataset_name}")
    print(f"Sequence Name: {data.sequence_name}")
    print(f"Delta Lidar position: {data.delta_pos_lidar}")
    print(f"Delta Lidar orientation: {data.delta_orient_lidar}")
    print(f"Lidar vertical fov: {data.intrinsics_lidar_new}")
    print(f"Lidar horizontal fov: {data.intrinsics_hoz_lidar_new}")
    print(f"Lidar vertical beams: {data.V_lidar_ch}")
    print(f"Lidar horizontal beams: {data.H_lidar_ch}")
    print(f"Lidar range: {data.Lidar_range}")
    print(f"Delta camera position: {data.delta_pos_cam}")
    print(f"Delta camera orientation: {data.delta_orient_cam}")
    print(f"Image Height: {data.image_H}")
    print(f"Image Width: {data.image_W}")

@app.post("/submit")
def submit_data(data: Data):
    output = capture_output(generate_output, data)
    return {"output": output}
