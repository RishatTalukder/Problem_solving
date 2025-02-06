class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        memo = {}
        candidates = [i for i in range(1, maxChoosableInteger + 1)]

        def dp(candidates, remaining):
            if candidates[-1] >= remaining:
                return True
            
            if candidates in memo:
                return memo[candidates]
            
            for i in range(len(candidates)):
                if not dp(candidates[:i] + candidates[i+1:], remaining - candidates[i]):
                    memo[candidates] = True
                    return True
                
            memo[candidates] = False
            return False
        
        if sum(candidates) < desiredTotal:
            return False
        
        return dp(tuple(candidates), desiredTotal)