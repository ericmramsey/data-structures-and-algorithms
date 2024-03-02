# Eric Ramsey
# CSCI 3102
# Module 6 Assignment - floyd_warshall_algorithm.py
# Spring 2024

# function used to implement the Floyd-Warshall algorithm to determine the shortest path between all pairs of node in a given graph
def floyd_warshall_algo(graph):
    # obtain all nodes contained in a given graph and store with established dictionary keys
    nodes = list(graph.keys())
    number_of_nodes = len(nodes) # establish the number of nodes contained on the graph
    
    # identify the nodes and their indices to create ease of access in matrix implementation
    node_index = {nodes[i]: i for i in range(number_of_nodes)}
    # initalize distance matrix and set the value of all non-diagonal connected node pairs to infinity
    distance = [[float('inf')] * number_of_nodes for _ in range(number_of_nodes)]
    
    # iterate through the established nodes on graph and construct matrix with the corresponding edge
    for node in graph:
        distance[node_index[node]][node_index[node]] = 0 # set distance if current node to 0 in reference to itself
        # iterate through nodes contained in matrix and update with their edge weight
        for node_neighbor, edge_weight in graph[node].items():
            distance[node_index[node]][node_index[node_neighbor]] = edge_weight
            
    # iterate through number_of_nodes to determine the shortest path of all node pairs
    for k in range(number_of_nodes):
        for i in range(number_of_nodes):
            for j in range(number_of_nodes):
                # If the path from i to j through k is shorter than the current path from i to j, set shortest path
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    # initalize dictionary to start and determine the shortest path of the node pairs                
    shortest_paths = {
        node: {nodes[j]: distance[i][j] for j in range(number_of_nodes)} # create key value pair for node pairs (nodes[j]: key identifier, distance[i][j]: shortest distance)- inner dictionary comprehension
        for i, node in enumerate(nodes) # iterate through matrix and list node indexes to create dict keys - outer dictionary comprehension
    }
    
    return shortest_paths