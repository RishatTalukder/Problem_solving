from collections import deque

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = ""
        n = len(pattern)
        stack = deque()

        for i in range(n+1):
            stack.append(i+1)
            if i == n or pattern[i] == 'I':
                while stack:
                    res += str(stack.pop())

        return res
    
sol = Solution()
print(sol.smallestNumber("IIIDIDDD")) # 126543789