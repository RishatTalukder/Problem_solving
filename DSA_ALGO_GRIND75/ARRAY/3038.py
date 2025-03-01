from collections import Counter, deque

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        nums = deque(nums)
        score = nums.popleft() + nums.popleft()
        count = 1
        n = len(nums)

        while n >= 2:
            sm = nums.popleft() + nums.popleft()
            if sm == score:
                count += 1
            else:
                break

            n -= 2

        return count

sol = Solution()

print(sol.maxOperations([2,2,3,2,4,2,3,3,1,3])) # 2