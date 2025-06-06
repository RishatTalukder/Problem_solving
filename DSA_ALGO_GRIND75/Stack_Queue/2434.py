from collections import deque
from collections import Counter
class Solution:
    def robotWithString(self, s: str) -> str:
        s = deque(s)
        c = Counter(s)
        res = []
        stack = []
        min_char = 'a'


        for ch in s:
            stack.append(ch)
            c[ch] -= 1

            while c[min_char] == 0:
                min_char = chr(ord(min_char) + 1)

            while stack and stack[-1] <= min_char:
                res.append(stack.pop())


        
        return ''.join(res) 