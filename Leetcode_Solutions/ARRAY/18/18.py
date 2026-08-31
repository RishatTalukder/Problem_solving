class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def k_sum(nums, target, k):
            res = []

            if not nums:
                return res

            avg = target//k

            if avg < nums[0] or nums[-1]<avg:
                return res

            if k  == 2:
                return two_sum(nums, target)

            for i in range(len(nums)):
                if  i == 0 or nums[i-1] != nums[i]:
                    for subset in k_sum(nums[i+1:], target-nums[i], k-1):
                        res.append([nums[i]]+subset)

            return res

        def two_sum(nums, target):
            res = []

            left, right = 0, len(nums)-1

            while left < right:
                curr = nums[left]+nums[right]

                if curr < target or (left > 0 and nums[left] == nums[left -1]):
                    left += 1

                elif curr > target or (
                    right < len(nums) -1 and nums[right] == nums[right +1 ]
                ):
                    right -= 1

                else:
                    res.append([nums[left], nums[right]])
                    left += 1
                    right -= 1

            return res

        nums.sort()

        return k_sum(nums, target, 4)
