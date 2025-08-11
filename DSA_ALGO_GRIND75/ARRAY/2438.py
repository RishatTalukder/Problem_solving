class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        powers = []
        i = 0
        while (1 << i) <= n:
            if n & (1 << i):
                powers.append(1 << i)
            i += 1
        
        results = []
        for l, r in queries:
            product = 1
            for j in range(l, r + 1):
                product *= powers[j]

            product %= MOD
            results.append(product)
        
        return results