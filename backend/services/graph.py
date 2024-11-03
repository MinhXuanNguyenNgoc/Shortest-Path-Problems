from entities.coordinate import Coordinate
from entities.edge import Edge
from entities.graph import Graph
from entities.result import GraphResult
from services.utils import edges as _edges, nodes

def get_graph() -> GraphResult:
    vertices = [Coordinate(id=index, latitude=lat, longitude=lon) for index, (lat, lon) in enumerate(nodes)]
    
    # Mapping from coordinates to corresponding id in vertices
    coord_to_id = { (vertex.latitude, vertex.longitude): vertex.id for vertex in vertices }
    
    edges = [
        Edge(
            source=Coordinate(
                id=coord_to_id[(coord1[0], coord1[1])], 
                latitude=coord1[0], 
                longitude=coord1[1]
            ),
            destination=Coordinate(
                id=coord_to_id[(coord2[0], coord2[1])], 
                latitude=coord2[0], 
                longitude=coord2[1]
            ),
            weight=distance
        )
        for coord1, coord2, distance in _edges
    ]
    
    return GraphResult(Graph(vertices, edges))