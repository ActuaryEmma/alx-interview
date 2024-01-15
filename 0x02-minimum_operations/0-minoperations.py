#!/usr/bin/env python3
""" Task 0 """


def minOperations(n):
    """  Minimum Operations """
    if n <= 1:
        return 0

    # dp[i] represents the minimum number of operations to get i 'H' characters
    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # No operations needed for 1 'H'

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0
