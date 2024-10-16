#!/usr/bin/python3
"""Minimum operations."""


def minOperations(n: int) -> int:
    """Minmum operations needed to get n H characters."""

    if n < 2:
        return 0
    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
