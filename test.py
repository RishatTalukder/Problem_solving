from collections import deque

nums = [4,3,2,6]
nums = deque(nums)
nums.rotate(-1)

print(nums)