class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        n = len(nums)
        right = n-1

        while left < right:
            sm = nums[left] + nums[right]

            if sm > target:
                right -= 1
            elif sm < target:
                left += 1

            else:
                return [left+1,right+1]
