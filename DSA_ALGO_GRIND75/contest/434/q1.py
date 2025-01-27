from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        summ_right = sum(nums)
        summ_left = 0

        count = 0
        diff = 0

        for i in range(len(nums)-1):
            summ_left += nums[i]
            summ_right -= nums[i]

            diff = abs(summ_left - summ_right)

            if diff%2 == 0:
                count += 1

        return count
    
sol = Solution()

print(sol.countPartitions([2,4,6,8]))