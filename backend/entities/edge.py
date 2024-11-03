from entities.coordinate import Coordinate

class Edge:
    def __init__(self, source: Coordinate, destination: Coordinate, weight: float):
        self.source = source
        self.destination = destination
        self.weight = weight