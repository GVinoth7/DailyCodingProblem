# You are given an array of integers representing coin denominations and a total amount of money. Write a function to compute the fewest number of coins needed to make up that amount. If it is not possible to make that amount, return null.
# For example, given an array of [1, 5, 10] and an amount 56, return 7 since we can use 5 dimes, 1 nickel, and 1 penny.
# Given an array of [5, 8] and an amount 15, return 3 since we can use 5 5-cent coins.

def fewest_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    print(f" dp : {dp}")
    for coin in coins:
        for i in range(coin, amount + 1):
            print(coin, i)
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else None

    
print(fewest_coins([1, 5, 10], 56))