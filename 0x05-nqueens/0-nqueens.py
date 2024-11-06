#!/usr/bin/env python3
""" The nqueens problem."""
import sys


def backtrack(r, n, cols, pos, neg, board):
    """created the module function."""

    if s == n:
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return
    for c in range(n):
        if c in cols or (s + c) in pos or (s - c) in neg:
            continue
        cols.add(c)
        pos.add(s + c)
        neg.add(s - c)
        board[r][c] = 1

        backtrack(s+1, n, cols, pos, neg, board)

        cols.remove(c)
        pos.remove(s + c)
        neg.remove(s - c)
        board[s][c] = 0


def nqueens(n):
    """solution to nqueens."""

    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
