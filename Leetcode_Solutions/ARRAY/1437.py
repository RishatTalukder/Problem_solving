class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if 1 not in nums:
            return True
        
        c = 0

        ind = nums.index(1)

        ind += 1

        for i in nums[ind:]:
            if i == 0:
                c += 1
            else:
                if c >= k:
                    c = 0
                else:
                    return False

        return True
    

#cleaner

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -1
        
        for i, val in enumerate(nums):
            if val == 1:
                if prev != -1 and i - prev - 1 < k:
                    return False
                prev = i
        
        return True
