from pydantic import BaseModel
from typing import List, Tuple

from models.coordinate import CoordinateViewModel

class EdgeViewModel(BaseModel):
    source: CoordinateViewModel
    destination: CoordinateViewModel
    weight: float
    
    class Config:
        from_attributes = True