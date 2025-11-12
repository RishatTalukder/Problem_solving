# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         i=0
#         while(i<len(nums)):
#             if nums[i]==0:
#                 nums.append(0)
#                 nums.remove(0)
#             i+=1


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        n = len(nums)

        while right+1<n:
            print(left,right)
            if nums[left] == 0:
                if nums[right+1] == 0:
                    right = right+1 
                else:
                    nums[left],nums[right+1] = nums[right+1],nums[left]
                    left += 1
                    right += 1

            else:
                left += 1
                right += 1


sol = Solution()
nums = [1,0]

sol.moveZeroes(nums)
print(nums)