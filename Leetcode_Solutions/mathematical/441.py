class Solution:
    def quadratic(self, n: int) -> int:
        return int((1 + (1 + 4*n)**0.5) / 2)-1
    
    def arrangeCoins(self, n: int) -> int:
        return self.quadratic(n*2)
    

sol = Solution()
print(sol.arrangeCoins(5)) # 2


from math import sqrt

class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        Returns the maximum number of complete rows of a staircase 
        that can be formed with 'n' coins.
        """
        return int((-1 + sqrt(1 + 8 * n)) // 2)
