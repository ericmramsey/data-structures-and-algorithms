# Eric Ramsey
# CSCI 3102
# Module 6 Assignment - bfs_algorithm.py
# Spring 2024
from collections import deque

# function used to implement Breadth-First Search (BFS) Traversal for a given graph
def bfs_algorithm(graph, start_node):
    visited_nodes = set() # initialize set to track visited nodes
    queue = deque([start_node]) # initialize queue to store current nodes and neighboring nodes
    traversal = [] # list used to store the order of BFS traversal
    
    while queue:
        current_node = queue.popleft() # dequeue current node from the queue
        
        if current_node not in visited_nodes:
            traversal.append(current_node)
            visited_nodes.add(current_node)
        
        if current_node in graph:
            for neighbor_node, _ in graph[current_node]: 
                if neighbor_node not in visited_nodes:
                    queue.append(neighbor_node)
    # print("Current BFS Traversal Path: ", traversal)
    # return final bfs traversal list
    return traversal