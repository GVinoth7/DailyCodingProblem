# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates 
# and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

def lowest_positive_integer(arr):
    arr = [i for i in arr if i>0]
    for item in sorted(arr):
        if item+1 not in arr:
            return item+1
    return None



print(lowest_positive_integer([3, 4, -1, 1]))