from pydantic import BaseModel
from typing import List

from models.coordinate import CoordinateViewModel

class PathViewModel(BaseModel):
    path: List[CoordinateViewModel]
    distance: float
    
    class Config:
        from_attributes = True