# Eric Ramsey
# CSCI 3202
# Module 2 Assignment - fibonacci.py
# Spring 2024

# function used to determine fibonacci validation using initial module 2 native algorithm (with negative input implementation)
def fibonacci(n):
    # determine the initial base case for n = 0 and consider negative input values
    if n == 0 or n < 0:
        return 0
    elif n == 1:
        return 1
    # call the fibonacci() function recursively 
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

# function used to implement the divide and conquer technique to determine fibonacci validation
def fibonacci_divide_conquer(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # initialize the variables required for first pair of fibonacci numbers in sequence to begin iteration
        a = 0 
        b = 1
        # initialize iteration to determine fibonacci number following n in the sequence
        for _ in range(2, n + 1):
            # increment the initialized variables following the fibonacci requirements of determining sum of preceding sequence numbers
            a, b = b, a + b
        return b
