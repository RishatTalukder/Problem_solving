class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        left = 0 
        right = len(nums) - 1
        counter = 0
        nums.sort()
        while left < right:
            if nums[left] + nums[right] == k:
                counter += 1
                left += 1
                right -= 1

            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1

        
        return counter


nums = [3,1,3,4,3]
k = 5

print(Solution().maxOperations(nums,k))