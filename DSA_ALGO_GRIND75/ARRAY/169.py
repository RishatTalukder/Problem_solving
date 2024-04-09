class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] += 1

            else:
                dic[num] = 1

        
        for key, value in dic.items():
            if value > n // 2:
                return key

nums = [3,2,3]
sol = Solution()

print(sol.majorityElement(nums))