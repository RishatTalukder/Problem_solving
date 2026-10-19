from bisect import bisect_left


class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()

        ind = bisect_left(nums, target)

        ans = []

        while ind < len(nums) and nums[ind] == target:
            ans.append(ind)
            ind += 1


        return ans