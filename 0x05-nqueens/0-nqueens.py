#!/usr/bin/python3
"""N-queens problem solution."""
import sys


def is_safe(board, row, col):
    """check if a queen can be placed on board[row][col]"""

    for i in range(row):
        if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                    return False
    return True

def solve_nqueens(n, row, board, solutions):
    """Use backtracking to place queens on the board."""

    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)
            board[row] = -1


def main():
    """Main entry point."""

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be at least 4")
        sys.exit(1)
    solutions = []
    board = [-1] * n
    solve_nqueens(n, 0, board, solutions)
    for solution in solutions:
        print(solution)
if __name__ == "__main__":
    main()
