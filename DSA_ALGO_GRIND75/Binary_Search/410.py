from typing import List

class Solution:
    def partition_count(self,nums,max_sum):
        count = 1
        curr_sum = 0

        for num in nums:
            if curr_sum+num <= maxx_sum:
                curr_sum += num
            else:
                count += 1
                curr_sum = num

        return count
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (high+ low)//2
            partitions = self.partition_count(nums, mid)

            if partitions > k:
                low = mid + 1

            else:
                high = mid - 1

        return low

sol = Solution()
nums = [7,2,5,10,8]
k = 2

print(sol.splitArray(nums, k))