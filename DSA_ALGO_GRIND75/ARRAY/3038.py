from collections import Counter, deque

from typing import List
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        nums = deque(nums)
        score = nums.popleft() + nums.popleft()
        count = 1
        n = len(nums)

        prev = True

        while n >=2 and prev:
            summ = nums[0] + nums[1]

            if summ == score:
                count += 1
            
            else:
                prev = False


            nums.popleft()
            nums.popleft()
            n -= 2 

        
        return count
    

sol = Solution()

print(sol.maxOperations([2,2,3,2,4,2,3,3,1,3])) # 2