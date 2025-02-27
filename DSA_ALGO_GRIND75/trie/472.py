class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        word_set = set(words)
        incorrect = set()

        def dfs(word):
            if word in word_set:
                return True
            
            elif word in incorrect:
                return False
            
            for i in range(1,len(word)):
                if word[:i] in word_set and dfs(word[i:]):
                        return True
                    
            incorrect.add(word)
            return False
                

        for word in words:
            word_set.remove(word)
            if dfs(word):
                res.append(word)

            word_set.add(word)