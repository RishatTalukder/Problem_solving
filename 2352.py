class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        column = [0]*len(grid)

        for i in range(len(grid[0])):
            