from collections import OrderedDict, Counter, deque
from math import gcd

def dfs_template(r, c, visited, condition_fn):
    """
    General DFS template for grid problems.

    Args:
        r, c: Current cell coordinates.
        visited: Set to track visited cells.
        condition_fn: A function that defines the condition to move to the next cell.
    """
    # Mark the current cell as visited
    visited.add((r, c))

    # Define possible directions (up, down, left, right)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Explore neighboring cells
    for dr, dc in directions:
        new_r, new_c = r + dr, c + dc

        # Check if the new cell is valid and meets the condition
        if (
            0 <= new_r < rows and           # Within row bounds
            0 <= new_c < cols and           # Within column bounds
            (new_r, new_c) not in visited and  # Not visited
            condition_fn(r, c, new_r, new_c)   # Satisfies the given condition
        ):
            dfs_template(new_r, new_c, visited, condition_fn)
