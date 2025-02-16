from fastapi import FastAPI, Depends, HTTPException
import joblib
from threading import Lock
import io
import sys
from pydantic import BaseModel
from functools import lru_cache

app = FastAPI()

# Singleton model instance via factory method using joblib
class NVSFModel:
    _instance = None
    _lock = None # Thread lock for synchronization
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    # Load the model during initialization
                    cls._instance = super().__new__(cls)
                    cls._instance.model = joblib.load("path/to/the/model")
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
    dataset_name: str
    sequence_name: str
    delta_pos_lidar: list[float]
    delta_orient_lidar: list[float]
    intrinsics_lidar_new: list[float]
    intrinsics_hoz_lidar_new: list[float]
    V_lidar_ch: int
    H_lidar_ch: int
    Lidar_range: float
    delta_pos_cam: list[float]
    delta_orient_cam: list[float]
    image_H: int
    image_W: int

# Function to capture terminal output
def capture_output(func, *args, **kwargs):
    buffer = io.StringIO()
    sys.stdout = buffer
    func(*args, **kwargs)
    sys.stdout = sys.__stdout__
    return buffer.getvalue()

# Caching function using lru_cache
@lru_cache(maxsize=10)  # Adjust maxsize as needed
def generate_output(data: InputData):
    key = f"{data.dataset_name}_{data.sequence_name}"

    # Load the NVSF model if it hasn't been loaded before
    # model = NVSFModel.get_model()
    model = model_singleton
    
    # Generate output based on the data and model
    result = capture_output(lambda d: model(d), data)
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
@app.post("/generate_output/")
async def generate_output_endpoint(data: InputData):
    try:
        result = generate_output(data)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)