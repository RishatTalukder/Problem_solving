from collections import deque

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        s = deque(s)
        part = list(part)
        n = len(part)
        stack_len = 0

        while s:
            stack.append(s.popleft())
            stack_len += 1

            if stack_len >= n and stack[-n:] == part:
                for _ in range(n):
                    stack.pop()
                    stack_len -= 1

        return ''.join(stack)