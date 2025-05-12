from collections import deque


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        stack = deque(map(int, s))

        while len(stack) > 2:
            new_s = deque()
            for i in range(len(stack) - 1):
                new_s.append((stack[i] + stack[i + 1]) % 10)

            stack = new_s

        return stack[0] == stack[1]