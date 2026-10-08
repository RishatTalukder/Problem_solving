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

