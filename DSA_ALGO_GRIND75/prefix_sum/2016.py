class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        mn = nums[0]


        for i in nums[1:]:
            if i > mn:
                res = max(res, i-mn)

            else:
                mn = i


        return res 