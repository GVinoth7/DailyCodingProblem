# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


def pair_sum(arr, k):
    unique_arr = list(set(arr))
    for item in arr:
            remaining_value = k - item
            if remaining_value in unique_arr:
                    return True
    return False
        

print(pair_sum([10,15,3, 17], 17))