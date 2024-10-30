# This file contains function to manage the graph theory

import heapq
from OSM import calculate_distance

def create_adjacency_matrix(nodes, edges):
    """
    Creates adjacency matrix based on the passed nodes and edges
    
    :param nodes: Array of nodes e.g. [(106.5455434,10.4554545),(...)]
    :param edges: Array of edges e.g. [(start_node,end_node,distance)]

    :return: 2D-Array representing the nodes and edges List[int][int]
    """
    num_nodes = len(nodes)
    adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    # Erstelle eine Mapping von Knoten zu Indizes
    node_to_index = {node: index for index, node in enumerate(nodes)}

    for edge in edges:
        from_node, to_node, distance = edge
        from_index = node_to_index[from_node]
        to_index = node_to_index[to_node]
        adjacency_matrix[from_index][to_index] = distance
        adjacency_matrix[to_index][from_index] = distance  # Für ungerichtete Graphen

    return adjacency_matrix

def create_minimum_spanning_tree(nodes):
    """
    Creates a minimum spanning tree using Prim's Algortihm
    
    :param nodes: A list of coordinates e.g. [(106.5455434,10.4554545),(...)]

    :return result: An Array containing the nodes and its edges in this format [(start_node,end_node,distance)] e.g. [((106.5455434,10.4554545),(106.5455454,10.4554598),210)]
    """
    num_nodes = len(nodes)
    if num_nodes == 0:
        return []

    # Min-Heap für die Kanten
    min_heap = []
    visited = [False] * num_nodes
    result = []

    # Starte mit dem ersten Knoten
    visited[0] = True
    edges_count = 0  # Zähler für die Anzahl der Kanten

    # Füge alle Kanten vom ersten Knoten zu den anderen Knoten hinzu
    for j in range(1, num_nodes):
        distance = calculate_distance(nodes[0], nodes[j])
        heapq.heappush(min_heap, (distance, 0, j))  # (Distanz, von, nach)

    while min_heap and edges_count < num_nodes - 1:
        distance, from_node, to_node = heapq.heappop(min_heap)
        if not visited[to_node]:
            visited[to_node] = True
            starting_node = (nodes[from_node][0], nodes[from_node][1])
            ending_node = (nodes[to_node][0], nodes[to_node][1])
            result.append((starting_node,ending_node, distance))
            edges_count += 1

            # Füge neue Kanten von dem neu besuchten Knoten hinzu
            for j in range(num_nodes):
                if not visited[j]:
                    new_distance = calculate_distance(nodes[to_node], nodes[j])
                    heapq.heappush(min_heap, (new_distance, to_node, j))

    return result

def path_to_coordinates(nodes, path):
    """
    This will return the coordinates based on the passed matrix indicies

    :param nodes: List of the nodes
    :param path: Array consisting of matrix indicies

    :return: Array of tuples containing the coordinates
    """
    result = []

    for i in path:
        result.append(get_coordinates_from_matrix_index(nodes, i))
    
    return result

def find_node_index(nodes, target_node):
    """
    Suche den Index eines Knotenpunkts in der Liste der Knotenpunkte.
    
    :param nodes: Liste der Knotenpunkte (Koordinaten)
    :param target_node: Der gesuchte Knotenpunkt (Koordinaten)
    :return: Der Index des gesuchten Knotenpunkts oder -1, wenn nicht gefunden
    """
    try:
        return nodes.index(target_node)
    except ValueError:
        return -1  # Knotenpunkt nicht gefunden

def get_coordinates_from_matrix_index(nodes, index):
    """
    Gibt die Koordinaten eines Knotenpunkts anhand seines Index in der Adjacency-Matrix zurück.
    
    :param nodes: Liste der Knotenpunkte (Koordinaten)
    :param index: Der Index des gesuchten Knotenpunkts in der Adjacency-Matrix
    :return: Die Koordinaten des Knotenpunkts oder None, wenn der Index ungültig ist
    """
    if 0 <= index < len(nodes):
        return nodes[index]
    else:
        return None  # Ungültiger Index