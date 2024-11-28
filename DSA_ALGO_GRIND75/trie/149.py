class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        memo = {}

        def dfs(start):
            if start == n:
                return True
            
            if start in memo:
                return memo[start]
            
            for end in range(start + 1, n + 1):
                if s[start:end] in word_set and dfs(end):
                    memo[start] = True
                    return True
                
            memo[start] = False
            return False
        
        return dfs(0)