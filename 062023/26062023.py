# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.


alpha_map = {str(a):chr(96+a) for a in range(1,27)}

def is_valid(code):
    """Check if a string can be decoded using alpha_map"""
    return code in alpha_map

def num_decodings(s):
    """Calculate the number of decodings"""
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # There's one way to decode an empty string

    # For each character from left to right
    for i in range(1, n + 1):
        # Try single character decoding
        if is_valid(s[i - 1:i]):
            dp[i] += dp[i - 1]
        # Try double character decoding (only if we have at least 2 characters)
        if i >= 2 and is_valid(s[i - 2:i]):
            dp[i] += dp[i - 2]
        
        print(f" The dp of i : {i} {dp[i]}")
    return dp[n]


print(num_decodings('1111'))