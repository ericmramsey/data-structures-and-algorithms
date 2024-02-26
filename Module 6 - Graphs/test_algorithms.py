# Eric Ramsey
# CSCI 3102
# Module 6 Assignment - test_algorithms.py
# Spring 2024
import unittest
from bfs_algorithm import bfs_algorithm

class TestAlgorithms(unittest.TestCase):
    # function used to resolve the AttributeError caused by graph not being initialized
    def setUp(self):
        self.initialize_test_graph()
        
    # function used to initialize the test bfs algorithm with graph given in the assignment
    def initialize_test_graph(self):
        # set the graph nodes with corresponding edge connection weights with neighboring nodes
        self.graph = {
            'a': [('b', 4), ('f', 2)],
            'b': [('a', 4), ('f', 1), ('c', 8)],
            'c': [('b', 8), ('d', 7), ('g', 2)],
            'd': [('c', 7), ('e', 9)],
            'e': [('f', 1), ('g', 6)],
            'f': [('a', 2), ('b', 1), ('e', 1), ('g', 7)],
            'g': [('c', 2), ('e', 6), ('f', 1)]
        }
        
    # function used to test the performance of bfs algorithm traversal against the expected traversal path of given graph
    def test_bfs(self):
        expected_traversal = ['a', 'b', 'f', 'c', 'e', 'g', 'd']
        actual_traversal = bfs_algorithm(self.graph, 'a')
        print('expected_traversal: ', expected_traversal)
        print('actual_traversal: ', actual_traversal)
        self.assertEqual(actual_traversal, expected_traversal)
    
# conditional used to allow testing to be run in terminal directly
if __name__ == '__main__':
    unittest.main()