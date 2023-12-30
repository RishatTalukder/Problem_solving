class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum == 0:
                    triplet = [nums[i], nums[left], nums[right]]
                    triplet.sort()

                    if triplet not in result:
                        result.append(triplet)

                    left += 1
                    right -= 1

                elif sum < 0:
                    left += 1

                else:
                    right -= 1

        return result