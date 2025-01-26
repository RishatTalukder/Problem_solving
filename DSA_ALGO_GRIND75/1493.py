class Solution:
    def longestSubarray(self, nums: list[int]) -> int:

        left, right, mx = 0, 0, 0
        zero_count = 0

        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1

            while zero_count> 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            mx = max(mx, right - left)

            right += 1

        return mx


nums = [1,1,1]
print(Solution().longestSubarray(nums))