class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9+7

        A= B = 6

        for _ in range(2,n+1):
            new_a = (3*A+2*B)  % MOD
            new_b = (2*A + 2*B) % MOD


            A = new_a
            B = new_b

        return (A+B) % MOD