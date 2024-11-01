import time
from typing import List, Tuple

from entities.path import Path
from entities.result import MultiplePathsResult
from services.dijkstra import dijkstra
from services.utils import path_to_coordinates

def remove_edge(adjacency_matrix: List[List[int]], u: int, v: int):
    """
    Removes an edge between nodes u and v in the given adjacency matrix.

    Parameters:
    adjacency_matrix (List[List[int]]): The adjacency matrix representing the graph.
    u (int): The index of the source node.
    v (int): The index of the target node.

    Returns:
    None: This function modifies the adjacency matrix in place; it does not return a value.
    """
    adjacency_matrix[u][v] = 0  # Remove the edge by setting its weight to 0

def restore_edge(adjacency_matrix: List[List[int]], u: int, v: int, weight: float) -> None:
    """
    Restores a previously removed edge between nodes u and v in the given adjacency matrix.

    Parameters:
    adjacency_matrix (List[List[int]]): The adjacency matrix representing the graph.
    u (int): The index of the source node.
    v (int): The index of the target node.
    weight (float): The weight of the edge to be restored.

    Returns:
    None: This function modifies the adjacency matrix in place; it does not return a value.
    """
    adjacency_matrix[u][v] = weight  # Restore the edge with its original weight

def yen_ksp(adjacency_matrix: List[List[int]], source: int, sink: int, K: int) -> List[List[int]]:
    """
    Finds the K-shortest paths between two nodes using Yen's K-Shortest Paths algorithm.

    Parameters:
    adjacency_matrix (List[List[int]]): The adjacency matrix representing the graph.
    source (int): The index of the source node.
    sink (int): The index of the target node.
    K (int): The number of shortest paths to find.

    Returns:
    List[List[int]]: A list of K shortest paths, where each path is represented as a list of node indices.
                     If fewer than K paths can be found, the list of found paths is returned.

    Raises:
    ValueError: If the adjacency matrix is not square or if the source or sink index is out of bounds.
    """
    # Step 0: Create a copy of the adjacency matrix to not change the original matrix
    adjacency_matrix = [row[:] for row in adjacency_matrix]
    # Step 1: Determine the shortest path from the source to the sink
    length, visited_vertices, path = dijkstra(adjacency_matrix, source, sink)
    A = [path]  # Store only the path
    B = []  # Initialize the set to store the potential k-th shortest paths

    for k in range(1, K):
        for i in range(len(A[k - 1]) - 1):
            spur_node = A[k - 1][i]
            root_path = A[k - 1][:i + 1]

            # Step 3: Remove edges for the paths that share the same root path
            removed_edges = []
            for p in A:
                if root_path == p[:i + 1]:
                    weight = adjacency_matrix[p[i]][p[i + 1]]
                    remove_edge(adjacency_matrix, p[i], p[i + 1])
                    removed_edges.append((p[i], p[i + 1], weight))  # Store removed edges for restoration

            # Step 4: Calculate the spur path from the spur node to the sink
            try:
                spur_length, spur_visited, spur_path = dijkstra(adjacency_matrix, spur_node, sink)

                if spur_path and spur_path[0] == spur_node:  # Ensure spur path is valid
                    total_path = root_path[:-1] + spur_path  # Avoid duplicate spur node

                    # Add the potential k-shortest path to the list if it's not already in A
                    if total_path not in A and total_path not in B:
                        B.append(total_path)

            except ValueError:
                # If no path is found, continue to the next iteration
                continue

            # Restore edges removed from the graph
            for u, v, weight in removed_edges:
                restore_edge(adjacency_matrix, u, v, weight)

        if not B:
            break

        # Sort the potential k-shortest paths by cost
        B.sort(key=lambda path: sum(adjacency_matrix[path[j]][path[j + 1]] for j in range(len(path) - 1)))

        # Add the lowest cost path to A
        A.append(B.pop(0))

    return A

def get_shortest_path(
    adjacency_matrix: List[List[int]], 
    nodes: List[Tuple[float, float]], 
    source_vertex: int, 
    destination_vertex: int,
    k: int
) -> MultiplePathsResult:
    start_time = time.perf_counter()
    path_list = yen_ksp(adjacency_matrix, source_vertex, destination_vertex, k)
    total_time = time.perf_counter() - start_time
    
    paths = []
    for path in path_list:
        coordinates = path_to_coordinates(nodes, path)
        paths.append(Path(coordinates, 0))
    
    return MultiplePathsResult(paths, total_time)