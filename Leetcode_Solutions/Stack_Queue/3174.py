class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        s = deque(s)

        while s:
            if s[0].isdigit():
                stack.pop()
                s.popleft()
            
            else:
                stack.append(s.popleft())

        return "".join(stack)