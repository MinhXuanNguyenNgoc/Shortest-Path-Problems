from pydantic import BaseModel
from typing import List

from models.coordinate import CoordinateViewModel
from models.path import PathViewModel

class SinglePathResultViewModel(BaseModel):
    result: PathViewModel
    elapsedTime: float
    
    class Config:
        from_attributes = True
        
class MultiplePathsResultViewModel(BaseModel):
    result: List[PathViewModel]
    elapsedTime: float
    
    class Config:
        from_attributes = True