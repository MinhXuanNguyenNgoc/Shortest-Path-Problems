from pydantic import BaseModel

class CoordinateViewModel(BaseModel):
    id: int
    latitude: float
    longitude: float
    
    class Config:
        from_attributes = True