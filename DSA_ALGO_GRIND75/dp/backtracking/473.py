class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        ln = sum(matchsticks)//4
        if ln*4 != sum(matchsticks):
            return False
        
        matchsticks.sort(reverse=True)
        sums = [0]*4

        def backtrack(idx):
            if idx == len(matchsticks):
                return sums[0] == sums[1] == sums[2] == sums[3]
            
            for i in range(4):
                if sums[i] + matchsticks[idx] <= ln:
                    sums[i] += matchsticks[idx]
                    if backtrack(idx+1):
                        return True
                    sums[i] -= matchsticks[idx]
            return False
        
        return backtrack(0)