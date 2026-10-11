class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        depth = 0

        for ch in s:
            if ch == '(':
                stack.append((depth, ch))
                depth += 1

            else:
                depth -= 1
                stack.append((depth, ch))

        res = ''
        for depth, ch in stack:
            if depth != 0:
                res += ch


        return res

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0

        ans = ''

        for ch in s:
            if ch == ')':
                depth -= 1

            if depth != 0:
                ans += ch
            
            if ch == '(':
                depth += 1


        return ans