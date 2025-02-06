from collections import deque
from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = deque()
        n = len(nums)
        minn = [0] * n
        minn[0] = nums[0]

        for i in range(1, n):
            minn[i] = min(minn[i - 1], nums[i])

        for i in range(n - 1, -1, -1):
            if nums[i] > minn[i]:
                while stack and stack[-1] <= minn[i]:
                    stack.pop()

                if stack and stack[-1] < nums[i]:
                    return True

                stack.append(nums[i])

        return False
    

sol = Solution()
# print(sol.find132pattern([1,3,4,2])) # False
# #bigger test case
print(sol.find132pattern([3,1,4,2,5,6,7,8,9,10])) # True