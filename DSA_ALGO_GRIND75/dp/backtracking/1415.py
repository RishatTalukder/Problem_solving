class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(s: str):
            nonlocal k
            if len(s) == n:
                k -= 1
                return s if k == 0 else ''
            
            for c in 'abc':
                if not s or s[-1] != c:
                    res = backtrack(s + c)
                    if res:
                        return res
        
        res = backtrack('')
        return res if res else ''