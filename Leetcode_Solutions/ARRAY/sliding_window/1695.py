class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res=0
        left = 0
        right =0
        dup = set()
        total = 0
        for right in range(len(nums)):
            while nums[right] in dup:
                total -= nums[left]
                dup.remove(nums[left])
                left += 1

            total += nums[right]
            dup.add(nums[right])
            res = max(res,total)

        return res