class Solution:
    def longestSubarray(self, nums: list[int]) -> int:

        l, mx = 0,0
        k = 1

        for r,n in enumerate(nums):
            k -= (1-n)

            if k<0:
                k += (1-nums[l])
                l += 1

            mx = max(mx,r-l)

        return mx


nums = [1,1,1]
print(Solution().longestSubarray(nums))