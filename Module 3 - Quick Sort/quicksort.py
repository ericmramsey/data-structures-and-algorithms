# Eric Ramsey
# CSCI 3102
# Module 3 Assignment - quicksort.py
# Spring 2024

# function used to partition the dataset
import random

# function used for sorting the elements of a dataset based on location of the pivot element selection
def partition(array, low, high):
    # set the first element of the dataset to pivot_selection
    pivot_selection = array[low]
    i = low + 1
    j = high

    # nested loop used to analyze and divide the elements of a dataset based on the set variable values and range of i and j
    for _ in range(i, j + 1):
        # loop used to search dataset from left to right to determine if value of i is > pivot_selection
        while i <= j and array[i] <= pivot_selection:
            i += 1
        # loop used to search dataset from right to left to determine if value of j is <= pivot_selection
        while i <= j and array[j] > pivot_selection:
            j -= 1
        # conditional used to replace the element assigned to i with the element assigned to j if i <= j
        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            break
    # assigns the pivot_selection element in its corresponding location
    array[low], array[j] = array[j], array[low]

    return j

# function used for sorting the elements of a dataset based on the median pivot element selection
def partition_median(array, low, high):
    # determine the median of the dataset elements
    median = (low + high) // 2
    # conditional statements used to adjust the elements of a dataset in ascending order (left to right)
    if array[low] > array[high]:
        array[low], array[high] = array[high], array[low]
    if array[median] > array[high]:
        array[median], array[high] = array[high], array[median]
    if array[low] > array[median]:
        array[low], array[median] = array[median], array[low]
    # set the first element of the dataset to pivot_selection
    pivot_selection = array[low]
    i = low + 1
    j = high

    # nested loop used to analyze and divide the elements of a dataset based on the set variable values and range of i and j
    for _ in range(i, j + 1):
        # loop used to search dataset from left to right to determine if value of i is > pivot_selection
        while i <= j and array[i] <= pivot_selection:
            i += 1
        # loop used to search dataset from right to left to determine if value of j is <= pivot_selection
        while i <= j and array[j] > pivot_selection:
            j -= 1
        # conditional used to replace the element assigned to i with the element assigned to j if i <= j
        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            break
    # assigns the pivot_selection element in its corresponding location
    array[low], array[j] = array[j], array[low]

    return j

# function used to implement quicksort algorithm using the initial pivot selection technique
def quicksort_pivot_selection(array, low, high):
    if low < high:
        pivot_selection = partition(array, low, high)
        quicksort_pivot_selection(array, low, pivot_selection - 1)
        quicksort_pivot_selection(array, pivot_selection + 1, high)

# function used to implement quicksort algorithm using the random selection technique
def quicksort_random_selection(array, low, high):
    if low < high:
        pivot_selection = random.randint(low, high)
        array[low], array[pivot_selection] = array[pivot_selection], array[low]

        pivot_selection = partition(array, low, high)
        quicksort_random_selection(array, low, pivot_selection - 1)
        quicksort_random_selection(array, pivot_selection + 1, high)

# function used to implement quicksort algorithm using the median of three technique
def quicksort_median_of_three(array, low, high):
    if low < high:
        pivot_selection = partition_median(array, low, high)

        quicksort_median_of_three(array, low, pivot_selection - 1)
        quicksort_median_of_three(array, pivot_selection + 1, high)


# resources: https://www.javatpoint.com/quicksort-in-python#:~:text=The%20Quicksort%20algorithm%20works%20by,equivalent%20to%20the%20pivot%20element.
#            https://www.youtube.com/watch?v=CB_NCoxzQnk
