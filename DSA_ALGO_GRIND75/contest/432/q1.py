class Solution:
    def zigzagTraversal(self, grid):
        for i in range(1,len(grid),2):
            grid[i] = grid[i][::-1]
        
        return_array = []

        for i in grid:
            return_array.extend(i)

        return return_array[::2]
    

sol = Solution()
print(sol.zigzagTraversal([[1,2,3],[4,5,6],[7,8,9]]))