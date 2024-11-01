import heapq
from math import inf
import time
from typing import List, Tuple

from entities.path import Path
from entities.result import SinglePathResult
from services.utils import path_to_coordinates

def dijkstra(adjacency_matrix: List[List[int]], start_index: int, destination_index: int):
    """
    Djikstra Algorithm implementation based on the slides in the lecture

    Parameters:
    adjacency_matrix (List[List[int]]): The adjacency matrix reprresenting the nodes and edges
    start_index (int): The index of the start node
    destination_index (int): The index of the destination node

    Returns:
    Tuple[int, List[int], List[int]]: A tuple containing:
        - The length of the shortest path (int).
        - What vertices were visited (List[int]).
        - The shortest path (List[int]).
    """
    # Error Handling: 
    # Check if all rows in the adjacency matrix are of equal length
    num_vertices = len(adjacency_matrix)
    if any(len(row) != num_vertices for row in adjacency_matrix):
        raise ValueError("All rows in the adjacency matrix must have the same number of vertices.") 
    # Validate start and destination indices
    if start_index < 0 or start_index >= num_vertices:
        raise IndexError(f"Start index {start_index} is out of bounds. Must be between 0 and {num_vertices - 1}.")
    if destination_index < 0 or destination_index >= num_vertices:
        raise IndexError(f"Destination index {destination_index} is out of bounds. Must be between 0 and {num_vertices - 1}.")

    # Step 1: Initialize
    S = set()  # Set of visited vertices
    visited_vertices = []  # List to track the order of visited vertices
    labels = [inf] * num_vertices  # All labels set to infinity
    labels[start_index] = 0  # Starting vertex label set to 0
    predecessors = [None] * num_vertices  # Track predecessors for path reconstruction

    # Priority queue to select the vertex with the smallest label
    priority_queue = [(0, start_index)]  # (label, vertex index)

    while priority_queue:
        # Step 2: Iteration
        current_label, u = heapq.heappop(priority_queue)  # Select next vertex
        if u in S:  # If already visited, skip
            continue
        S.add(u)  # Add to the visited set
        visited_vertices.append(u)  # Track the visited vertex

        # Update labels for each vertex v not in S
        for v in range(num_vertices):
            weight = adjacency_matrix[u][v]
            if weight > 0 and v not in S:  # Only consider vertices not yet visited and with an edge
                # Calculate new label
                new_label = labels[u] + weight
                # Update label and predecessor if the new label is smaller
                if new_label < labels[v]:
                    labels[v] = new_label
                    predecessors[v] = u  # Update predecessor for path reconstruction
                    heapq.heappush(priority_queue, (new_label, v))  # Push updated label to priority queue

        # Step 3: Repeat until destination is in S
        if destination_index in S:
            break

    # Check if destination was reached
    if labels[destination_index] == inf:
        raise ValueError(f"There is no path from vertex {start_index} to vertex {destination_index}.")

    # Reconstruct the shortest path
    path = []
    current_vertex = destination_index
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = predecessors[current_vertex]
    path.reverse()

    # Final label of destination vertex
    return labels[destination_index], visited_vertices, path


def get_shortest_path(
    adjacency_matrix: List[List[int]], 
    nodes: List[Tuple[float, float]], 
    source_vertex: int, 
    destination_vertex: int
) -> SinglePathResult:
    start_time = time.perf_counter()
    distance, nodes_visited, path = dijkstra(adjacency_matrix, source_vertex, destination_vertex)
    total_time = time.perf_counter() - start_time
    
    coordinates = path_to_coordinates(nodes, path)
    
    return SinglePathResult(Path(coordinates, distance), total_time)