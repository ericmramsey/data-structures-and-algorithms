# Eric Ramsey
# CSCI 3102
# Module 4 Assignment - greedy.py
# Spring 2024

def knapsack_max_value(carry_capacity, weight, value):
    # determine if len(weight) and len(value) meet the requirement of both being equal length
    if len(weight) != len(value):
        raise ValueError("lengths of weight and value lists do not meet equal length requirement.")
    
    # initialize the value of len(weight) and set variable n
    n = len(weight)

    # determine the value-to-weight ratio for each element in the given datasets for future step actions
    value_weight_ratio = [(value[i] / weight[i], weight[i], value[i]) for i in range(n)]
    value_weight_ratio.sort(reverse=True) # sort the ratio values in descending order

    # initialize solution variable max_value  and increment variable available_carry_capacity
    max_value = 0
    available_carry_capacity = carry_capacity

    # implement greedy algorithm and iterate through list items until available_carry_capacity of knapsack is considered full
    for value_weight_ratios, weights, values in value_weight_ratio:
        if available_carry_capacity >= weights:
            max_value += values
            available_carry_capacity -= weights
        else:
            # break out of loop process if available_carry_capacity is not able to accept another item completely
            max_value += available_carry_capacity * value_weight_ratios
            break
    
    return max_value
