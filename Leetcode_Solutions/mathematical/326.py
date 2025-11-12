class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n != 1:
            if n%3 in [1,2] or n==0:
                return False

            n //= 3

        return True