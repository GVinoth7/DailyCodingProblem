# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

def largest_sum(arr):
    if not arr:
        return 0
    
    length = len(arr)
    
    # Base cases
    max_sums = [0] * length
    
    if length > 1:
        max_sums[1] = max(max_sums[0], arr[1])
        
    for i in range(2, length):
        max_sums[i] = max(max_sums[i-1], max_sums[i-2]+arr[i])
        
    
    print(max_sums)
    return max_sums[-1]
        
    
print(largest_sum([2, 4, 6, 2, 5]))