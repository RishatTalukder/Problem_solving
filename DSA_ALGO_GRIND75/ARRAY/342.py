class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n != 1:
            if (n % 4 != 0) or n == 0:
                return False
            n //= 4
        return True