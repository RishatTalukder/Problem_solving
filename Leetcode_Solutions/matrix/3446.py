from collections import defaultdict
from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        hashmap = defaultdict(list)
        rows = len(grid)
        cols = len(grid[0])

        # Group elements by diagonal (key = row - col)
        for row in range(rows):
            for col in range(cols):
                key = row - col
                hashmap[key].append(grid[row][col])

        # Sort each diagonal
        for key in hashmap:
            if key < 0:
                hashmap[key].sort(reverse=True)
            else:
                hashmap[key].sort()

        # Refill the matrix with sorted diagonals
        for row in range(rows):
            for col in range(cols):
                key = row - col
                grid[row][col] = hashmap[key].pop()

        return grid