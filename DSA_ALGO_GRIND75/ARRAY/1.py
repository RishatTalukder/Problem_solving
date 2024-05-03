# class Solution:
#     def twoSum(self, nums, target):
#         dic = {}

#         for ind, num in enumerate(nums):
#             if num in dic:  # If the complement of the current number is already in the dictionary
#                 return [dic[num], ind]  # Return the indices of the two numbers
#             else:
#                 dic[target - num] = ind  # Store the complement and its index in the dictionary


class Solution:
    def twoSum(self, nums, target: int) :
        index_list = [0]*len(nums)

        for i in range(len(nums)):
            diff = target-nums[i]
            if nums[i] in index_list: 
                return [i,index_list.index(nums[i])]
                

            else:
                index_list[i] = diff
             
        return None
    
sol = Solution()
print(sol.twoSum([2,7,11,15],9)) # [0,1]
print(sol.twoSum([3,2,4],6)) # [1,2]