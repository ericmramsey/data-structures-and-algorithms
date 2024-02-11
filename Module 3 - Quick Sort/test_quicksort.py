# Eric Ramsey
# CSCI 3102
# Module 3 Assignment - test_quicksort.py
# Spring 2024

import unittest
import quicksort
import time

class TestQuickSort(unittest.TestCase):

    def test_quicksort_pivot_selection(self):
        '''test function used to determine accuracy of Quick Sort using original pivot selection technique.'''
        test_array = [32, 5, 22, 40, 7]
        start_time = time.time()
        quicksort.quicksort_pivot_selection(test_array, 0, len(test_array) - 1)
        end_time = time.time()
        total_time = end_time - start_time
        print("quicksort_pivot_selection running time: ", total_time, " seconds")
        self.assertEqual(test_array, sorted(test_array))

    def test_quicksort_random_selection(self):
        '''test function used to determine accuracy of Quick Sort using random selection technique.'''
        test_array = [32, 5, 22, 40, 7]
        start_time = time.time()
        quicksort.quicksort_random_selection(test_array, 0, len(test_array) - 1)
        end_time = time.time()
        total_time = end_time - start_time
        print("quicksort_random_selection running time: ", total_time, " seconds")
        self.assertEqual(test_array, sorted(test_array))
    
    def test_quicksort_median_of_three(self):
        '''test function used to determine accuracy of Quick Sort using median of three technique.'''
        test_array = [32, 5, 22, 40, 7]
        start_time = time.time()
        quicksort.quicksort_median_of_three(test_array, 0, len(test_array) - 1)
        end_time = time.time()
        total_time = end_time - start_time
        print("quicksort_median_of_three running time: ", total_time, " seconds")
        self.assertEqual(test_array, sorted(test_array))

if __name__ == "__main__":
    unittest.main()
