class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        depth = 0
        ans = 0

        for i, ch in enumerate(s):
            if ch == '(':
                depth += 1

            else:
                depth -= 1

                if s[i-1] == '(':
                    ans += 1<<depth


        return ans


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)

            else:
                current = stack.pop()

                if current == 0:
                    current = 1

                else:
                    current *= 2


                stack[-1] += current

        return stack[-1]