class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)

        dp = [0]*n

        res = float('-inf')

        for i in range(n-1,-1,-1):
            dp[i] = energy[i] + (dp[i+k] if i+k < n else 0)
            res = max(res, dp[i])

        return res



class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        for i in range(n-1,-1,-1):
            if i + k < n:
                energy[i] += energy[i+k]
        return max(energy)
    
