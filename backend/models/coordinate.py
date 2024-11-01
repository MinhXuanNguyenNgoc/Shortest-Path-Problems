from pydantic import BaseModel

class CoordinateViewModel(BaseModel):
    latitude: float
    longitude: float
    
    class Config:
        from_attributes = True