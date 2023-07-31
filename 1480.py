class Solution:
    def runningSum(self, nums):
        for ind,val in enumerate(nums):
            if ind == 0 :
                pass 

            else:
               nums[ind] = nums[ind]+nums[ind-1]

        
        return nums


nums =[3,1,2,10,1]

print(Solution().runningSum(nums))
            