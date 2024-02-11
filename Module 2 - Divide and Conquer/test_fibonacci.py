# Eric Ramsey
# CSCI 3202
# Module 2 Assignment - test_fibonacci.py
# Spring 2024

import unittest
import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        '''Test function used to determine accuracy of fibonacci() algorithm'''
        self.assertEqual(fibonacci.fibonacci(0), 0)
        self.assertEqual(fibonacci.fibonacci(1), 1)
        self.assertEqual(fibonacci.fibonacci(2), 1)
        self.assertEqual(fibonacci.fibonacci(3), 2)
        self.assertEqual(fibonacci.fibonacci(4), 3)
        self.assertEqual(fibonacci.fibonacci(5), 5)

    def test_fibonacci_divide_conquer(self):
        '''Test function used to determine accuracy of fibonacci_divide_conquer() algorithm'''
        self.assertEqual(fibonacci.fibonacci_divide_conquer(0), 0)
        self.assertEqual(fibonacci.fibonacci_divide_conquer(1), 1)
        self.assertEqual(fibonacci.fibonacci_divide_conquer(2), 1)
        self.assertEqual(fibonacci.fibonacci_divide_conquer(3), 2)
        self.assertEqual(fibonacci.fibonacci_divide_conquer(4), 3)
        self.assertEqual(fibonacci.fibonacci_divide_conquer(5), 5)
        self.assertEqual(fibonacci.fibonacci_divide_conquer(6), 8)
        self.assertEqual(fibonacci.fibonacci_divide_conquer(7), 13)
        self.assertEqual(fibonacci.fibonacci_divide_conquer(8), 21)
        self.assertEqual(fibonacci.fibonacci_divide_conquer(9), 34)
        self.assertEqual(fibonacci.fibonacci_divide_conquer(10), 55)

    def test_fibonacci_divide_conquer_negative(self):
        '''Test function used to determine accuracy of fibonacci_divide_conquer() when negative input occurs'''
        self.assertEqual(fibonacci.fibonacci(-1), 0)
        self.assertEqual(fibonacci.fibonacci(-5), 0)
        self.assertEqual(fibonacci.fibonacci(-10), 0)
        self.assertEqual(fibonacci.fibonacci_divide_conquer(-1), 0)
        self.assertEqual(fibonacci.fibonacci_divide_conquer(-5), 0)
        self.assertEqual(fibonacci.fibonacci_divide_conquer(-10), 0)

# conditional used to allow testing to be run directly with terminal python test_calc.py and in editor -- if you run this module directly run unittest.main
if __name__ == '__main__':
    unittest.main()
