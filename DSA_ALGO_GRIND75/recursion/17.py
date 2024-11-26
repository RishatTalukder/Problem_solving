class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": "abc", "3": "def", "4": "ghi", 
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        if digits:
            return []

        combinations = []
        res = []

        def dfs(ind):
            if ind >= len(digits):
                res.append("".join(combinations))   
                return 

            for letter in letters[digits[ind]]:
                combinations.append(letter)
                dfs(ind+1)
                combinations.pop()

        dfs(0)

        return res  