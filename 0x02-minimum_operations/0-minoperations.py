#!/usr/bin/env python3
"""Minimum operations."""


def minOperations(n: int) -> int:
    """Minmum operations needed to get n H characters."""

    nxt = 'H'
    body = 'H'
    oper = 0
    while (len(body) < n):
        if n % len(body) == 0:
            oper += 2
            nxt = body
            body += body
        else:
            oper += 1
            body += nxt
    if len(body) != n:
        return 0
    return oper
