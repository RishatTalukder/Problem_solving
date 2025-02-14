from collections import OrderedDict, Counter, deque
from math import gcd

def subsets(nums: List[int]) -> List[List[int]]:
    """
    Generate all possible subsets of a given set of numbers.

    Args:
        nums: A list of integers.

    Returns:
        A list of all possible subsets.
    """
    def backtrack(start, path):
        # Add the current subset to the result
        res.append(path[:])

        # Generate all possible subsets
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    res = []
    backtrack(0, [])
    return res

def subset_2(nums: List[int]) -> List[List[int]]:
    subsets = []
    res = []

    def backtrack(start):
        if start == len(nums):
            subsets.append(res[:])
            return
        
        res.append(nums[start])
        backtrack(start + 1)
        res.pop()
        backtrack(start + 1)

    backtrack(0)
    return subsets


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


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": "abc", "3": "def", "4": "ghi", 
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        subset = subsets([letters[digit] for digit in digits])
        return ["".join(s) for s in subset if s]