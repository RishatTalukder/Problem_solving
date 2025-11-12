class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        curr, prev, k2 = 1, 0, k*2
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                curr += 1

            else:
                prev, curr = curr, 0

            if (curr >= k and prev >= k) or curr >= k2:
                return True
            
        return False