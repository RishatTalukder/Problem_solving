class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0

        left = 0
        right = 0
        while right < len(nums):
            

            if nums[right] - nums[left] <= k:
                right += 1
            else:
                res += 1
                left = right


        return res + 1