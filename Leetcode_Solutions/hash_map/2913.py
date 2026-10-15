class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            subset = set()

            for j in range(i, len(nums)):
                subset.add(nums[j])
                ans += len(subset)**2


        return ans