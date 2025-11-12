from typing import List

class Solution:
    def get_subsequences(self, nums, index, k, subsequence):
        
        if index == len(nums):
            if len(subsequence) <= k:
                return [subsequence[:]]
            return []
        
        result = []
        
        # Include the current element
        subsequence.append(nums[index])
        result += self.get_subsequences(nums, index + 1, k, subsequence)
        subsequence.pop()  # Backtrack

        # Exclude the current element
        result += self.get_subsequences(nums, index + 1, k, subsequence)

        return result



    def minMaxSums(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        nums.sort()
        subsequences = self.get_subsequences(nums, 0, k, [])
        minn = 0
        maxx = 0
        
        for subsequence in subsequences:
            if subsequence:
                minn += subsequence[0]
                maxx += subsequence[-1]

        return (minn + maxx) % MOD

