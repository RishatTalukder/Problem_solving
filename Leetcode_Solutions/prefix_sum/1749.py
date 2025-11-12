class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mn = 0
        mx = 0
        total = 0

        for num in nums:
            total += num
            mn = min(mn,total)
            mx = max(mx,total)

        return mx-mn