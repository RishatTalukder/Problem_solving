class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = n-1

            while left < right:
                sm = nums[left] + nums[right] + nums[i]

                if sm > 0 :
                    right -=1

                elif sm < 0:
                    left += 1
                    
                else:
                    res.add((nums[i],nums[left],nums[right]))
                    left += 1
                    right -= 1

        return list(res)
                    
                    

    

sol = Solution()
print(sol.threeSum([0,0,0,0])) # [[0,0,0]]