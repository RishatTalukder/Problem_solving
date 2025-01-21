class Solution:
    def gridGame(self, grid):
        top_row_sum = sum(grid[0])
        bottom_row_sum = 0
        min_max_sum = float('inf')
        
        for i in range(len(grid[0])):
            top_row_sum -= grid[0][i]
            min_max_sum = min(min_max_sum, max(top_row_sum, bottom_row_sum))
            bottom_row_sum += grid[1][i]
        
        return min_max_sum
    

grid = [[2,5,4],[1,5,1]]
sol = Solution()
print(sol.gridGame(grid)) # 4