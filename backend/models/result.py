from pydantic import BaseModel
from typing import List

from models.path import PathViewModel
from models.graph import GraphViewModel

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

class GraphResultViewModel(BaseModel):
    result: GraphViewModel
    
    class Config:
        from_attributes = True