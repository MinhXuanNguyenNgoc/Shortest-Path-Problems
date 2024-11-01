from typing import List

from entities.path import Path

class SinglePathResult:
    def __init__(self, result: Path, elapsedTime: float):
        self.result = result
        self.elapsedTime = elapsedTime
        
class MultiplePathsResult:
    def __init__(self, result: List[Path], elapsedTime: float):
        self.result = result
        self.elapsedTime = elapsedTime