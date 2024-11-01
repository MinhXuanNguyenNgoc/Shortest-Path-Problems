import os
import OSM
import graph
import belman_ford
import time
from dijkstra import dijkstra
from yen import yen_ksp


def main():
    # Step 1.1: Get the intersections inbetween HCMUT and Sheraton Hotel
    # Because the Google Map API is not capable to return intersections in an area (and is really expensive), i have used openstreetmaps (OSM) instead
    # With OSM, I have extracted the intersections with the function "OSM.extract_nodes_from_osm_file"
    # Because this will result in over 3600 intersections, I had to clean the nodes to get back a total of 107 nodes.
    # These nodes were saved into the "intersections.csv" file
    # So we will use this csv file to get the nodes of the intersections 
    __osm_location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    nodes = OSM.read_from_csv(path=os.path.join(__osm_location__, "intersections.csv"))

    # Step 1.2: Add hcmut and sheraton coordinates to the nodes
    # TODO: Instead of hardcoding these coordinates, we can pass them via the api
    hcmut_cords = (10.772055, 106.657826)
    sheraton_cords = (10.775440, 106.703864)
    nodes.append(hcmut_cords)
    nodes.append(sheraton_cords)

    # Step 2: Create edges
    # First we create a minimum spanning tree to make sure, that all nodes are connected with each other
    # Because we want to have several paths from the start to the end (k-path), a minimum spanning tree would result
    # in only one path, thus we add one more edges. For this case, I will look for 40% of all nodes for the 2 nearest neighbours 
    # and create an edge to them too to create several paths.
    edges = graph.create_minimum_spanning_tree(nodes)
    graph.nearest_neighbour(nodes,edges,0.4)

    # Optional: Visualize Graph
    #G = debug.debug_create_graph(nodes,edges)
    #debug.debug_show_graph(G)

    # Step 3: Create adjacency matrix
    matrix = graph.create_adjacency_matrix(nodes,edges)

    # Step 4: Get index of hcmut and sheraton hotel
    index_hcmut = graph.find_node_index(nodes, hcmut_cords)
    index_sheraton = graph.find_node_index(nodes, sheraton_cords)

    # Step 5: Dijkstra
    start_time_dijkstra = time.perf_counter()
    dijkstra_shortest_path_length, dijkstra_visited, dijkstra_path = dijkstra(matrix, index_hcmut, index_sheraton)
    total_time_dijkstra = time.perf_counter() - start_time_dijkstra

    # Step 6: Belman-Ford
    start_time_belman = time.perf_counter()
    belman_distance, belman_preprocessor = belman_ford.bellman_ford(matrix, index_hcmut)
    belman_path = belman_ford.shortest_path(belman_preprocessor,index_hcmut,index_sheraton)
    total_time_belman = time.perf_counter() - start_time_belman

    # Step 7: Floyd Warshall
    # TODO: Implement

    # Step 8: Evaluate performance times
    # TODO: Return the result to the api endpoint
    print("Performance Dijkstra: {}".format(total_time_dijkstra))
    print("Performance Belman-Ford: {}".format(total_time_belman))

    # Step 9: Translate the path to its coordinates
    dijkstra_coordinates = graph.path_to_coordinates(nodes,dijkstra_path)
    belman_coordinates = graph.path_to_coordinates(nodes,belman_path)

    # Step 10: Print out results
    # TODO: Return this result to the API Endpoint
    print("Shortest Path from HCMUT to Sheraton Hotel with Dijkstra: {}".format(dijkstra_path))
    print("Shortest Path from HCMUT to Sheraton Hotel with Belman-Ford: {}".format(belman_path))

    # Step 11: k shortest path using Yen's algorithm
    yen_result = yen_ksp(matrix,index_hcmut,index_sheraton,3)
    print(yen_result)

if __name__ == "__main__":
    main()