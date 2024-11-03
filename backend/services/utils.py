import csv
import os
from typing import List, Tuple, Optional

from entities.coordinate import Coordinate

def write_matrix_to_csv(matrix: List[List[float]], path: str) -> None:
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in matrix:
            writer.writerow(row)

def read_nodes_from_csv(path: str) -> List[Tuple[float, float]]:
    nodes = []
    with open(path, mode ='r') as file:
        csvFile = csv.reader(file)
        skip = True
        for lines in csvFile:
            if skip:
                skip = False
                continue
            nodes.append((float(lines[0]),float(lines[1])))
    
    return nodes

def read_edges_from_csv(path: str) -> List[Tuple[Tuple[float, float], Tuple[float, float], float]]:
    edges = []
    with open(path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for line in csv_reader:
            coord1 = (float(line[0]), float(line[1]))
            coord2 = (float(line[2]), float(line[3]))
            distance = float(line[4])
            edges.append((coord1, coord2, distance))
    return edges

def read_matrix_from_csv(path: str) -> List[List[float]]:
    matrix = []
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            matrix.append([float(value) for value in row]) 
    return matrix

def find_node_index(nodes: List[Tuple[float, float]], target_node: Tuple[float, float]) -> int:
    try:
        return nodes.index(target_node)
    except ValueError:
        return -1

def get_coordinates_from_matrix_index(nodes: List[tuple], index: int) -> Optional[Coordinate]:
    if 0 <= index < len(nodes):
        latitude, longitude = nodes[index]
        return Coordinate(index, latitude, longitude)
    else:
        return None

def path_to_coordinates(nodes: List[tuple], path: List[int]) -> List[Coordinate]:
    """
    This will return the coordinates based on the passed matrix indices.

    :param nodes: List of the nodes
    :param path: Array consisting of matrix indices

    :return: List of Coordinate objects containing the coordinates
    """
    result = []

    for i in path:
        result.append(get_coordinates_from_matrix_index(nodes, i))
    
    return result

nodes = read_nodes_from_csv(os.path.join(os.getcwd(), "data", "intersections.csv"))
edges = read_edges_from_csv(os.path.join(os.getcwd(), "data", "edges.csv"))
adjacency_matrix = read_matrix_from_csv(os.path.join(os.getcwd(), "data", "adjacency_matrix.csv"))

hcmut_cords = (10.772055, 106.657826)
sheraton_cords = (10.775440, 106.703864)

nodes.append(hcmut_cords)
nodes.append(sheraton_cords)

index_hcmut = find_node_index(nodes, hcmut_cords)
index_sheraton = find_node_index(nodes, sheraton_cords)