
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

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def dp(open, close, s):
            if open == n and close == n:
                res.append(s)
                return

            
            if open < n:
                dp(open+1, close, s+'(')

            if close < open:
                dp(open, close+1, s+')')

            

        dp(0,0,'')

        return res