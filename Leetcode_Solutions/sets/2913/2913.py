class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            sub = set()

            for j in range(i, len(nums)):
                sub.add(nums[j])
                ans += len(sub)**2


        return ans