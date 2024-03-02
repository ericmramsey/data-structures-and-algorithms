# Eric Ramsey
# CSCI 3102
# Module 6 Assignment - test_floyd_warshall_algorithm.py
# Spring 2024
from floyd_warshall_algorithm import floyd_warshall_algo
import unittest

class TestFloydWarshallAlgorithm(unittest.TestCase):
    def test_floydwarshall_algorithm(self):
        # initialize the graph and nodes with corresponding edge weights
        graph = {
            'a': {'b': 4, 'c': 11},
            'b': {'a': 6, 'c': 2},
            'c': {'a': 3}
        }
        
        expected_shortest_pairs_path = {
            'a': {'a': 0, 'b': 4, 'c': 6}, 
            'b': {'a': 5, 'b': 0, 'c': 2}, 
            'c': {'a': 3, 'b': 7, 'c': 0}
        }
    
        result = floyd_warshall_algo(graph)
        self.assertEqual(result, expected_shortest_pairs_path)
        print('results: ', result)

# conditional used to allow testing to be run in terminal directly
if __name__ == '__main__':
    unittest.main()