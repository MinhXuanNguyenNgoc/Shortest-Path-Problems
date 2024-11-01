from typing import List, Tuple

from entities.path import Path
from entities.result import SinglePathResult
from services.utils import path_to_coordinates

def get_shortest_path(
    adjacency_matrix: List[List[int]], 
    nodes: List[Tuple[float, float]], 
    source_vertex: int, 
    destination_vertex: int
) -> SinglePathResult:
    
    return SinglePathResult(Path([], 0), 0)