from pydantic import BaseModel
from typing import List, Tuple

from models.coordinate import CoordinateViewModel
from models.edge import EdgeViewModel

class GraphViewModel(BaseModel):
    vertices: List[CoordinateViewModel]
    edges: List[EdgeViewModel]
    
    class Config:
        from_attributes = True