class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = nums[0]
        for i in range(len(nums)):
            if curr_sum+nums[i] < nums[i]:
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]
                
            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum
    

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ## divide and conquer
        def max_crossing_sum(nums, left, right, mid):
            left_sum = float('-inf')
            curr_sum = 0
            for i in range(mid, left-1, -1):
                curr_sum += nums[i]
                left_sum = max(left_sum, curr_sum)
                
            right_sum = float('-inf')
            curr_sum = 0
            for i in range(mid+1, right+1):
                curr_sum += nums[i]
                right_sum = max(right_sum, curr_sum)
                
            return left_sum + right_sum
        
        def max_sub_array(nums, left, right):
            if left == right:
                return nums[left]
            
            mid = (left+right)//2
            left_sum = max_sub_array(nums, left, mid)
            right_sum = max_sub_array(nums, mid+1, right)
            cross_sum = max_crossing_sum(nums, left, right, mid)
            
            return max(left_sum, right_sum, cross_sum)
        
        return max_sub_array(nums, 0, len(nums)-1)
    