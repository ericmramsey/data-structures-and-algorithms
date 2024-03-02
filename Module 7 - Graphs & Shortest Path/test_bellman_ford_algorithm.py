# Eric Ramsey
# CSCI 3102
# Module 6 Assignment - test_bellman_ford_algorithm.py
# Spring 2024

from bellman_ford_algorithm import bellman_ford_algo
import unittest

class TestBellmanFordALgorithm(unittest.TestCase):
    # test function used to initialize the test of Bellman-Ford Algorithm for determining shortest path for graph1
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
            'b': 25,
            'c': 10,
            'd': 25,
            'e': 35,
            'f': float('inf')
        }
        
        result = bellman_ford_algo(graph1, 'a')
        self.assertEqual(result, expected_shortest_path)
        print('test_graph1: ', result)
        
    # test function used to initialize the test of Bellman-Ford Algorithm for determining shortest path for graph2
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
            'c': 6
        }
        
        result = bellman_ford_algo(graph2, 'a')
        print('test_graph1 results: ', result)
        self.assertEqual(result, expected_shortest_path)
        print('test_graph2: ', result)
        
    # test function used to determine bellman_ford_algo function's efficiency when handling a graph with negative edge weights
    def test_graph_negative_edge_weights(self):
        # initialize the graph and nodes with corresponding edge weights
        graph = {
            'a': {'b': -1, 'c': 4},
            'b': {'c': 3, 'd': 2, 'e': 2},
            'c': {},
            'd': {'b': 1, 'c': 5},
            'e': {'d': -3}
        }
        # Define the expected shortest path from the starting node of the given graph - node 'a'
        expected_shortest_path = {
            'a': 0,
            'b': -1,
            'c': 2,
            'd': -2,
            'e': 1
        }
        
        result = bellman_ford_algo(graph, 'a')
        self.assertEqual(result, expected_shortest_path)
        print('test_graph_negative_edge_weights: ', result)
        
    # test function used to determine bellman_ford_algo function's efficiency when handling a graph with negative cycle
    def test_graph_negative_cycle(self):
        # initialize the graph and nodes with corresponding edge weights containing negative cycle
        graph = {
            'a': {'b': 1},
            'b': {'c': -2},
            'c': {'a': -1}
        }
        
        with self.assertRaises(ValueError):
            bellman_ford_algo(graph, 'a')
        
# conditional used to allow testing to be run in terminal directly
if __name__ == '__main__':
    unittest.main()