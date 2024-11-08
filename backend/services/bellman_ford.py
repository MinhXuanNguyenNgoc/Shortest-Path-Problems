from math import inf
import time
from typing import List, Tuple

from entities.path import Path
from entities.result import SinglePathResult
from services.utils import path_to_coordinates

def bellman_ford(adjacency_matrix: List[List[int]], source_vertex: int) -> Tuple[List[int], List[int]]:
    """
    Bellman-Ford Algorithm implementation based on the slides in the lecture

    Parameters:
    adjacency_matrix (List[List[int]]): A 2D list where the element at row i and column j represents the weight of the edge from vertex i to vertex j.
    source_vertex (int): The index of the start node

    Returns:
    Tuple[List[int], List[int]]: A tuple containing:
        - shortest distances from the source vertex to each vertex (List[int]).
        - keeps track of the previous vertex for each vertex in the shortest path (List[int]).
    
    Raises:
    - ValueError: If the adjacency matrix contains inconsistent row lengths.
    - IndexError: If the source vertex index is out of bounds.
    """
    # Error Handling: 
    # Check if all rows in the adjacency matrix are of equal length
    num_vertices = len(adjacency_matrix)
    if any(len(row) != num_vertices for row in adjacency_matrix):
        raise ValueError("All rows in the adjacency matrix must have the same number of vertices.") 
    # Validate source vertex index
    if source_vertex < 0 or source_vertex >= num_vertices:
        raise IndexError(f"Source index {source_vertex} is out of bounds. Must be between 0 and {num_vertices - 1}.")

    # Step 1: Initialize
    distance = [inf] * num_vertices
    distance[source_vertex] = 0
    predecessor = [None] * num_vertices

    # Step 2: Iteration
    for _ in range(num_vertices - 1):
        for u in range(num_vertices):
            for v in range(num_vertices):
                weight = adjacency_matrix[u][v]
                if weight > 0 and distance[u] != inf and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    predecessor[v] = u

    # Step 3: Check for negative cycles (Optional)
    for u in range(num_vertices):
        for v in range(num_vertices):
            weight = adjacency_matrix[u][v]
            if weight > 0 and distance[u] != inf and distance[u] + weight < distance[v]:
                raise ValueError("Graph contains a negative cycle")

    return distance, predecessor

def shortest_path(predecessor: List[int], source_vertex: int, destination_vertex: int) -> List[int]:
    """
    Reconstructs the shortest path from the source vertex to the destination vertex
    using the predecessor list generated by `bellman_ford`.

    Parameters:
        predecessor (List[int]): A list that contains the previous vertex for each vertex in the shortest path.
        source_vertex (int): The starting vertex index.
        destination_vertex (int): The target vertex index for which to reconstruct the path.

    Returns:
        path (List[int]): A list of vertex indices representing the shortest path from source to destination.

    Raises:
    - ValueError: If there is no path from the source vertex to the destination vertex.
    """
    path = []
    current_vertex = destination_vertex
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = predecessor[current_vertex]
    path.reverse()
    if path[0] != source_vertex:
        raise ValueError("No path from source vertex to destination vertex")
    return path

def get_shortest_path(
    adjacency_matrix: List[List[int]], 
    nodes: List[Tuple[float, float]], 
    source_vertex: int, 
    destination_vertex: int
) -> SinglePathResult:
    start_time = time.perf_counter()
    distance, preprocessor = bellman_ford(adjacency_matrix, source_vertex)
    path = shortest_path(preprocessor, source_vertex, destination_vertex)
    elapsed_time = time.perf_counter() - start_time
    
    coordinates = path_to_coordinates(nodes, path)
    
    return SinglePathResult(Path(coordinates, distance[destination_vertex]), elapsed_time)
    