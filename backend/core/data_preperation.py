import haversine as hs   
from haversine import Unit

NODE_DISTANCE = 200
'''
The minimum distance between each node
'''


def calculate_distance(coordinate1, coordinate2):
    return int(hs.haversine(coordinate1,coordinate2,unit=Unit.METERS))

def prepare(nodes):
    '''
    This function will take in all found nodes/intersections and will clean up the nodes, so that the
    minimum distance between each node is NODE_DISTANCE. If the distance of one node to another is smaller
    than NODE_DISTANCE, it will be discarded.

    :return: 
    Depending on NODE_DISTANCE, less than the total nodes will be returned.
    '''
    
    nodes_copy = nodes[:]
    clean_nodes = []
    next_node = False
    # iterate nodes
    for startNode in nodes_copy:
        if clean_nodes.count(startNode) >= 1:
            continue
        for endNode in nodes_copy:
            if startNode == endNode:
                continue
            else:
                # look for all nodes within the radius of NODE_DISTANCE
                if calculate_distance(startNode,endNode) <= NODE_DISTANCE:
                    # first node found
                    if not next_node:
                        clean_nodes.append(startNode)
                        next_node = True
                        continue
                    else:
                        # node already found --> discard all next nodes within NODE_DISTANCE
                        try:
                            nodes_copy.remove(startNode)
                        except ValueError:
                            continue
        next_node = False

    return clean_nodes