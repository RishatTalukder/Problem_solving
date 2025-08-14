class Solution:
    def largestGoodInteger(self, num: str) -> str:
        count = 0
        prev = 'X'   # sentinel value
        maxd = ' '   # store max digit found
        
        for c in num:
            if c == prev:
                count += 1
            else:
                count = 1
            if count == 3:
                maxd = max(c, maxd)
            prev = c
        
        return "" if maxd == ' ' else maxd * 3