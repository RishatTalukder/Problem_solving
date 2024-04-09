class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum,right_sum = 0,sum(nums)

        for i,val in enumerate(nums):
            right_sum -= val

            if left_sum == right_sum:
                return i 
            
            left_sum += val


nums = [1,7,3,6,5,6]
print(Solution().pivotIndex(nums))
