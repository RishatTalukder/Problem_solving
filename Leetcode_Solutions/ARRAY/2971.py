class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        perimeter = sum(nums)
        for i in range(len(nums)):
            perimeter -= nums[i]

            if perimeter > nums[i]:
                return perimeter + nums[i]

        return -1

