#!/usr/bin/python3
"""function that will return the island parameter of the island described."""


def island_perimeter(grid):
    """grid is a list of integers."""

    perimeter = 0
    rows = len(grid)
    if rows > 0:
        cols = len(grid[0])
    else:
        cols = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
