# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
# For example, if N is 4, then there are 5 unique ways:
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.


def count_unique_ways(n, steps):
    if n<=0:
        return 0
    
    dp = [0] * (n+1)
    
    dp[0]=1
    
    # Calculate the unique ways
    
       # Calculate the unique ways using dynamic programming
    for i in range(1, n + 1):
        for step in steps:
            if i >= step:
                dp[i] += dp[i - step]

    return dp[n]




n = 4
steps = {1, 2}
print(count_unique_ways(n, steps))  #