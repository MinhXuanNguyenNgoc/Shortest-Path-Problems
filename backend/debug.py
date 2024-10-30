# file containing debug functions to visualize the results

import networkx as nx
import matplotlib.pyplot as plt

def debug_create_graph(nodes, edges):
    """
    Creates a graph object based on the passed nodes and edges

    :param nodes: Array of nodes e.g. [(106.5455434,10.4554545),(...)]
    :param edges: Array of edges e.g. [(start_node,end_node,distance)]

    :return: networkx graph
    """
    # create graph
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(edges)
    
    return G

def debug_show_graph(G):
    """
    Visualize a networkx graph

    :param G: A networkx Graph
    """
    weight = nx.get_edge_attributes(G, "weight")
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, with_labels=True,pos=pos,node_size=500, node_color="r", edge_color="g",font_size=16)
    nx.draw_networkx_edge_labels(G,pos=pos,edge_labels=weight,font_size=16)
    plt.show()