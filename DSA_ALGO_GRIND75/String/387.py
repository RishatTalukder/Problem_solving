class Solution:
    def firstUniqChar(self, s: str) -> int:
        non_repeat = {}

        for ind,val in enumerate(s):
            if val in non_repeat:
                non_repeat[val] = "repeat"

            else:
                non_repeat[val] = ind
        
        for i in non_repeat:
            if non_repeat[i] != 'repeat':
                return non_repeat[i]

        return -1