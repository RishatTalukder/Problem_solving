class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)

        for i, val in enumerate(nums):
            right_sum -= val

            if right_sum == left_sum:
                return i

            left_sum += val

        return -1


nums = [1,7,3,6,5,6]
print(Solution().pivotIndex(nums))
