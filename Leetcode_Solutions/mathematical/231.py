
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 2

        if n == 1:
            return True
        
        while x < n:
            x *= 2
            if x == n:
                return True
            
        return False