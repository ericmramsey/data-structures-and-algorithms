# Eric Ramsey
# CSCI 3102
# Module 6 Assignment - bellman_ford_algorithm.py
# Spring 2024

# function used to determine 
def bellman_ford_algo(graph, start_node):
    # initialize start node distance as 0 and infinity for the remaining nodes
    distance = {node: float('inf') for node in graph}
    distance[start_node] = 0
    # iterate through nodes contained in given graph |V -1| times to determine shortest path implement relaxation principle
    for _ in range(len(graph) - 1):
        for node in graph:
            for node_neighbor, edge_weight in graph[node].items():
                # determine if the distance to the neighbor can be shortened and update the distance accordingly
                if distance[node] + edge_weight < distance[node_neighbor]:
                    distance[node_neighbor] = distance[node] + edge_weight
                    
    # determine if given graph contains a negative cycle and return ValueError accordingly
    for node in graph:
        for node_neighbor, edge_weight in graph[node].items():
            if distance[node] + edge_weight < distance[node_neighbor]:
                raise ValueError("The graph contains a negative cycle.")
                  
    return distance
