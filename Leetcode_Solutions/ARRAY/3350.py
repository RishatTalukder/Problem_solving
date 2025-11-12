class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        cur, prev, ans = 1, 0, 0

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                cur += 1

            else:
                prev, cur = cur, 1

            ans = max(ans, min(cur, prev))
            ans = max(ans, cur // 2)

        return ans