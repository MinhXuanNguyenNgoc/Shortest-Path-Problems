from typing import List, Tuple

from entities.coordinate import Coordinate
from entities.edge import Edge

class Graph:
    def __init__(self, vertices: List[Coordinate], edges: List[Edge]):
        self.vertices = vertices
        self.edges = edges