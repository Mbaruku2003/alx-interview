#!/usr/bin/python3
"""function that gives the change."""


def makeChange(coins, total):
    """If the total is 0 or less return 0."""

    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[total] == float('inf'):
        return -1
    return dp[total]