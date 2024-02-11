# Eric Ramsey
# CSCI 3102
# Module 4 Assignment - test_greedy.py
# Spring 2024

import unittest
import time
from greedy import knapsack_max_value

class TestGreedy(unittest.TestCase):

    def test_greedy_1(self):
        ''' test function used to determine solution to the given knapsack problem '''
        # initialize required variables to accurate test greedy algorithm function efficiency
        carry_capacity = 33
        weight = [5, 20, 10, 40]
        value = [100, 300, 300, 400]
        start_time = time.time()
        max_value = knapsack_max_value(carry_capacity, weight, value)
        end_time = time.time()
        total_time = end_time - start_time
        print("solution = ", max_value, "$")
        print("test_greedy_1 runtime: ", total_time, " seconds")
        self.assertEqual(knapsack_max_value(carry_capacity, weight, value), 670)


    def test_greedy_2(self):
        ''' test function used to determine the accuracy and efficiency of knapsack_max_value '''
        # initialize required variables to accurate test greedy algorithm function efficiency
        carry_capacity = 50
        weight = [10, 20, 30]
        value = [60, 100, 120]
        start_time = time.time()
        knapsack_max_value(carry_capacity, weight, value)
        end_time = time.time()
        total_time = end_time - start_time
        print("test_greedy_2 runtime: ", total_time, " seconds")
        self.assertEqual(knapsack_max_value(carry_capacity, weight, value), 240)

    def test_greedy_empty_knapsack(self):
        ''' test function used to determine the accuracy and efficiency of knapsack_max_value 
            when the knapsack contains no carry_capacity and still remains accurate
        '''
        # initialize required variables to accurate test greedy algorithm function efficiency
        carry_capacity = 0
        weight = [6, 11, 44]
        value = [100, 300, 400]
        start_time = time.time()
        knapsack_max_value(carry_capacity, weight, value)
        end_time = time.time()
        total_time = end_time - start_time
        print("test_greedy_empty_knapsack: ", total_time, " seconds")
        self.assertEqual(knapsack_max_value(carry_capacity, weight, value), 0)

    def test_greedy_single_carry_capacity(self):
        ''' test function used to determine the accuracy and efficiency of knapsack_max_value 
            when there is only a single item that meets carry_capacity requirements
        '''
        # initialize required variables to accurate test greedy algorithm function efficiency
        carry_capacity = 22
        weight = [22]
        value = [222]
        start_time = time.time()
        knapsack_max_value(carry_capacity, weight, value)
        end_time = time.time()
        total_time = end_time - start_time
        print("test_greedy_single_carry_capacity: ", total_time, " seconds")
        self.assertEqual(knapsack_max_value(carry_capacity, weight, value), 222)

    def test_greedy_equal_value_weight_ratio(self):
        ''' test function used to determine the accuracy and efficiency of knapsack_max_value 
            when an equal value_weight_ratio situation occurs
        '''
        # initialize required variables to accurate test greedy algorithm function efficiency
        carry_capacity = 10
        weight = [2, 3, 4]
        value = [10, 15, 20]
        start_time = time.time()
        knapsack_max_value(carry_capacity, weight, value)
        end_time = time.time()
        total_time = end_time - start_time
        print("test_greedy_equal_value_weight_ratio runtime: ", total_time, " seconds")
        self.assertEqual(knapsack_max_value(carry_capacity, weight, value), 45)

if __name__ == "__main__":
    unittest.main()
    