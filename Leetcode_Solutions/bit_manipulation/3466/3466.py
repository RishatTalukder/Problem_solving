class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1

        for i, v in enumerate(nums):
            if i != v:
                k &= v

        return 0 if k == -1 else k