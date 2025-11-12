class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        cache = {}

        def dfs(s):
            if s in cache:
                return cache[s]
            
            if s in word_set:
                return True
            
            for i in range(1, len(s)):
                pre = s[:i]

                if pre in word_set and dfs(s[i:]):
                    cache[pre] = True
                    return cache[pre]
                

            cache[s] = False
            return cache[s]
        

        return dfs(s)