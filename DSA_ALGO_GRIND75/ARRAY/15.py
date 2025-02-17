class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for ind,val in enumerate(nums):
            if ind > 0 and nums[ind] == nums[ind-1]:
                continue

            left = ind+1
            right = len(nums)-1

            while left < right:
                sum3 = val + nums[left] + nums[right]

                if sum3 > 0:
                    right -= 1
                
                elif sum3 < 0:
                    left += 1

                else:
                    res.append([val,nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        
        return res
                    
                    

    

sol = Solution()
print(sol.threeSum([0,0,0,0])) # [[0,0,0]]