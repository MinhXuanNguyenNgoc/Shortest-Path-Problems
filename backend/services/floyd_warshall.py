import time
from typing import List, Tuple

from entities.path import Path
from entities.result import SinglePathResult
from services.utils import path_to_coordinates


def floyd_warshall(adjacency_matrix: List[List[int]], start_index: int, destination_index: int) -> Tuple[int, List[int]]:
    """
    Floyd-Warshall Algorithm implementation based on the slides in the lecture

    Parameters:
    adjacency_matrix (List[List[int]]): The adjacency matrix reprresenting the nodes and edges
    start_index (int): The index of the start node
    destination_index (int): The index of the destination node

    Returns:
    Tuple[int, List[int], List[int]]: A tuple containing:
        - The length of the shortest path (int).
        - The shortest path (List[int]).
    """
    
    num_vertices = len(adjacency_matrix)
    
    # Initialize distances and next vertex matrix
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    next_vertex = [[None] * num_vertices for _ in range(num_vertices)]

    # Set initial distances and next vertices
    for i in range(num_vertices):
        for j in range(num_vertices):
            if adjacency_matrix[i][j] != 0:  # Edge exists
                dist[i][j] = adjacency_matrix[i][j]
                next_vertex[i][j] = j
            if i == j:
                dist[i][j] = 0

    # Floyd-Warshall algorithm
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_vertex[i][j] = next_vertex[i][k]

    # Reconstruct the shortest path
    path = []
    if next_vertex[start_index][destination_index] is None:
        return path  # No path exists

    current = start_index
    while current != destination_index:
        path.append(current)
        current = next_vertex[current][destination_index]
        if current is None:
            return []  # No path exists

    path.append(destination_index)
    return dist[start_index][destination_index], path

def get_shortest_path(
    adjacency_matrix: List[List[int]], 
    nodes: List[Tuple[float, float]], 
    source_vertex: int, 
    destination_vertex: int
) -> SinglePathResult:
    start_time = time.perf_counter()
    distance, path = floyd_warshall(adjacency_matrix, source_vertex, destination_vertex)
    elapsed_time = time.perf_counter() - start_time
    
    coordinates = path_to_coordinates(nodes, path)
    
    return SinglePathResult(Path(coordinates, distance), elapsed_time)