# Eric Ramsey
# CSCI 3102
# Module 6 Assignment - test_dijkstra_algorithm.py
# Spring 2024
from dijkstra_algorithm import dijkstra_algorithm
import unittest

class TestDijkstraAlgorithm(unittest.TestCase):
        # test function used to initialize the test of Dijkstra Algorithm for determining shortest path for graph1
    def test_graph1(self):
        # initialize the graph and nodes with corresponding edge weights
        graph1 = {
            'a': {'b': 50, 'c': 10, 'e': 45},
            'b': {'c': 15, 'e': 10},
            'c': {'a': 20, 'd': 15},
            'd': { 'b': 0, 'e': 35},
            'e': {'d': 39},
            'f': {'d': 3}
        }
        # Define the expected shortest path from the starting node of the given graph - node 'a'
        expected_shortest_path = {
            'a': 0, 
            'b': 50, 
            'c': 10, 
            'd': float('inf'), 
            'e': 45, 
            'f': float('inf')
        }
        
        result = dijkstra_algorithm(graph1, 'a')
        self.assertEqual(result, expected_shortest_path)
        print('test_graph1: ', result)
        
    # test function used to initialize the test of Dijkstra Algorithm for determining shortest path for graph2
    def test_graph2(self):
        # initialize the graph and nodes with corresponding edge weights
        graph2 = {
            'a': {'b': 4, 'c': 11},
            'b': {'a': 6, 'c': 2},
            'c': {'a': 3}
        }
        # Define the expected shortest path from the starting node of the given graph - node 'a'
        expected_shortest_path = {
            'a': 0, 
            'b': 4, 
            'c': 11
        }
        
        result = dijkstra_algorithm(graph2, 'a')
        self.assertEqual(result, expected_shortest_path)
        print('test_graph2: ', result)
        
    # test function used to initialize the test of Dijkstra Algorithm 
    def test_disconnected_graph(self):
        # initialize the graph and nodes with corresponding edge weights
        graph = {
            'a': {'b': 3},
            'b': {}, 
            'c': {}
        }
        # Define the expected shortest path from the starting node of the given graph - node 'a'
        expected_shortest_path = {
            'a': 0, 
            'b': 3, 
            'c': float('inf')
        }
        
        result = dijkstra_algorithm(graph, 'a')
        self.assertEqual(result, expected_shortest_path)
        print('test_disconnected_graph: ', result)
    
# conditional used to allow testing to be run in terminal directly
if __name__ == '__main__':
    unittest.main()