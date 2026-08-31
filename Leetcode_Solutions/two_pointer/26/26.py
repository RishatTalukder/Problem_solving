class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)  == 1:
            return 1

        slow = 1
        prev = nums[0]
        
        for  i in range(1,len(nums)):
            if nums[i] != prev:
                nums[slow] =  nums[i]
                slow += 1
                prev = nums[i]


        return slow