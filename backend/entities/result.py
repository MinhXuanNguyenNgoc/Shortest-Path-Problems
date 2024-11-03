from typing import List

from entities.graph import Graph
from entities.path import Path

class SinglePathResult:
    def __init__(self, result: Path, elapsedTime: float):
        self.result = result
        self.elapsedTime = elapsedTime
        
class MultiplePathsResult:
    def __init__(self, result: List[Path], elapsedTime: float):
        self.result = result
        self.elapsedTime = elapsedTime
        
class GraphResult:
    def __init__(self, result: Graph):
        self.result = result