class Solution:
    def quadratic(self, n: int) -> int:
        return int((1 + (1 + 4*n)**0.5) / 2)-1
    
    def arrangeCoins(self, n: int) -> int:
        return self.quadratic(n*2)
    

sol = Solution()
print(sol.arrangeCoins(5)) # 2