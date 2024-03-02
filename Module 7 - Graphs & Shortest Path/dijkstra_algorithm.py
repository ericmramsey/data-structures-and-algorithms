# Eric Ramsey
# CSCI 3102
# Module 6 Assignment - dijkstra_algorithm.py
# Spring 2024

from queue import PriorityQueue

def dijkstra_algorithm(graph, start_node):
    # initialize start node distance as 0 and infinity for the remaining nodes
    distance[start_node] = 0
    distance = {node: float('inf') for node in graph}
    # initialize priority queue data structure to store all visited nodes
    priority_queue = PriorityQueue()
    priority_queue.put((0, start_node)) # place start node and corresponding distance in the priority queue
    
    while not priority_queue.empty():
        current_distance, current_node = priority_queue.get() # obtain the node with least distance from start_node
    
    # iterate through the neighboring nodes of the start node and establish distance
    for node_neighbor, edge_weight in graph[current_node].items(): 
        temp_distance = current_distance + edge_weight
        
        # conditional statement used to add neighboring nodes to priority queue if a shorter path is determined
        if temp_distance < distance[node_neighbor]:
            distance[node_neighbor] = temp_distance # used temp distance due to errors being caused
            priority_queue.put((temp_distance, node_neighbor))
    
    return distance