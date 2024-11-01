from typing import List

from entities.coordinate import Coordinate

class Path:
    def __init__(self, path: List[Coordinate], distance: float):
        self.path = path
        self.distance = distance