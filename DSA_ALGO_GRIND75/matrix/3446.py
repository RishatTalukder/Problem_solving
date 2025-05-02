from collections import defaultdict
from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonals = defaultdict(list)

        # Step 1: Group all elements by their diagonal index (row - col)
        for row in range(n):
            for col in range(n):
                diag_key = row - col
                diagonals[diag_key].append(grid[row][col])

        # Step 2: Sort each diagonal:
        #         - If diagonal key is negative, sort in descending order
        #         - Else, sort in ascending order
        for diag_key in diagonals:
            if diag_key < 0:
                diagonals[diag_key].sort(reverse=True)
            else:
                diagonals[diag_key].sort()

        # Step 3: Write the sorted diagonals back into the grid
        for row in range(n):
            for col in range(n):
                diag_key = row - col
                grid[row][col] = diagonals[diag_key].pop()

        return grid
