from fastapi import FastAPI, Depends, HTTPException
import joblib
from threading import Lock
import io
import sys
from pydantic import BaseModel, Field
from functools import lru_cache
import threading

app = FastAPI()

# Singleton model instance via factory method using joblib
class NVSFModel:
    _instance = None
    _lock = None  # Thread lock for synchronization
    lock = threading.Lock()  # Correctly initialize the lock

    def __new__(cls):
        if cls._instance is None:
            with cls.lock:  # Use the class-level lock
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    # cls._instance.model = joblib.load("path/to/the/model") 
                    cls._instance.model = None  # TODO for testing purposes
        return cls._instance

# class NVSFModel:
#     @staticmethod
#     def get_model():
#         if not hasattr(NVSFModel, 'model'):
#             # Load the model from disk (assuming it's pickled)
#             NVSFModel.model = joblib.load("path/to/the/model")
#         return NVSFModel.model

# Create an instance of ModelSingleton
model_singleton = NVSFModel()

# Define the input data structure using Pydantic
class InputData(BaseModel):
    dataset_name: str = Field(default="dataset1", description="Name of the dataset")
    sequence_name: str = Field(default="sequence1", description="Name of the sequence")
    delta_pos_lidar: list[float] = Field(default=[0.0, 0.0, 0.0], description="Delta position (x, y, z) of the lidar in camera coordinates")
    delta_orient_lidar: list[float] = Field(default=[0.0, 0.0, 0.0], description="Delta orientation (roll, pitch, yaw) of the lidar in camera coordinates")
    intrinsics_lidar_new: list[float] = Field(default=[0.0, 0.0], description="Vertical intrinsics of the lidar")
    intrinsics_hoz_lidar_new: list[float] = Field(default=[0.0, 0.0], description="Horizontal intrinsics of the lidar")
    V_lidar_ch: int = Field(default=0, description="Number of vertical beams in the lidar")
    H_lidar_ch: int = Field(default=0, description="Number of horizontal beams in the lidar")
    Lidar_range: float = Field(default=0.0, description="Range of the lidar")
    delta_pos_cam: list[float] = Field(default=[0.0, 0.0, 0.0], description="Delta position (x, y, z) of the camera")
    delta_orient_cam: list[float] = Field(default=[0.0, 0.0, 0.0], description="Delta orientation (roll, pitch, yaw) of the camera")
    image_H: int = Field(default=0, description="Height of the image")
    image_W: int = Field(default=0, description="Width of the image")

# Function to capture terminal output
def capture_output(func, *args, **kwargs):
    buffer = io.StringIO()
    sys.stdout = buffer
    func(*args, **kwargs)
    sys.stdout = sys.__stdout__
    return buffer.getvalue()

# Caching function using lru_cache
@lru_cache(maxsize=10)  # Adjust maxsize as needed
def query_model(data: InputData):
    key = f"{data.dataset_name}_{data.sequence_name}"

    # Load the NVSF model if it hasn't been loaded before
    # model = NVSFModel.get_model() 
    model = model_singleton # TODO for testing purposes
    
    # Generate output based on the data and model
    # result = capture_output(lambda d: model(d), data)
    result = "test output"
    return {"result": result}

# Endpoint to provide help information (GET request)
@app.get("/help")
def get_help():
    return {
        "description": """
        This API provides usage instructions for generating output based on input parameters.
        The model is loaded once and cached to avoid redundant predictions with the same inputs.
        """
    }

# Endpoint that uses caching
@app.post("/generate/")
async def generate(data: InputData):
    try:
        result = query_model(data)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    # uvicorn run app:app --reload --port 8000 --host 0.0.0.0