
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        def dp(s, open, close):
            if len(s) == 2*n:
                ans.append(s)
                return 

            if open < n:
                dp(s+'(', open + 1, close)

            if close < open:
                dp(s+')', open, close + 1)

        dp('', 0, 0)

        return ans