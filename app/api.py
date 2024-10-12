from fastapi import FastAPI
from pydantic import BaseModel, Field
import io
import sys
from typing import List

app = FastAPI()

class Data(BaseModel):
    dataset_name: str = Field(description= " Name of the Dataset ")
    sequence_name: str = Field(description= " Name of the Sequence ")
    delta_pos_lidar: List[float] = Field(description= " Change in the Position of Lidar sensor in m ")
    delta_orient_lidar: List[float] = Field(description= " Change in the Orientation of Lidar sensor in degree ")
    intrinsics_lidar_new: List[float] = Field(description= " New Vertical Intrinsic parameter of Lidar ")
    intrinsics_hoz_lidar_new: List[float] = Field(description= " New horizontal Intrinsic paramter of Lidar ")
    V_lidar_ch: int = Field(description= " Vertical beams of Lidar ")
    H_lidar_ch: int = Field(description= " Horizontal beams of Lidar ")
    Lidar_range: float = Field(description= " Range of Lidar in m ")
    delta_pos_cam: List[float] = Field(description= " Change in the Position of Camera in m ")
    delta_orient_cam: List[float] = Field(description= " Change in the Orientation of Camera in m ")
    image_H: int = Field(description= " New Height of Camera sensor ")
    image_W: int = Field(description= " New Width of Camera sensor ")

# Function to capture terminal output
def capture_output(func, *args, **kwargs):
    buffer = io.StringIO()
    sys.stdout = buffer
    func(*args, **kwargs)
    sys.stdout = sys.__stdout__
    return buffer.getvalue()

# Function to print data for output generation
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

# Endpoint to provide help information (GET request)
# @app.get("/help")
# def get_help():
#     help_text = """
#     This API allows you to submit lidar and camera configuration data.
    
#     Endpoint /submit expects the following fields in JSON:
#     - dataset_name: str
#     - sequence_name: str
#     - delta_pos_lidar: List[float]
#     - delta_orient_lidar: List[float]
#     - intrinsics_lidar_new: List[float]
#     - intrinsics_hoz_lidar_new: List[float]
#     - V_lidar_ch: int
#     - H_lidar_ch: int
#     - Lidar_range: float
#     - delta_pos_cam: List[float]
#     - delta_orient_cam: List[float]
#     - image_H: int
#     - image_W: int

#     Use POST method on /submit with the above fields to get the formatted output.
#     """
#     return {"help": help_text}

# Endpoint to process and return the data (POST request)
@app.post("/submit")
def submit_data(data: Data):
    output = capture_output(generate_output, data)
    return {"output": output}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)