class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums = [(ind, num) for ind, num in enumerate(nums)]

        nums = sorted(nums, key=lambda x: -x[1])[:k]

        nums = sorted(nums)

        return [num[1] for num in nums]