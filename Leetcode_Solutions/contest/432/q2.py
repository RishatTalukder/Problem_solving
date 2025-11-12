class Solution:
    def maximumAmount(self, coins) -> int:
        #find the trwo smallest values
        
        
        count = 0
        for i in range(len(coins)):
            for j in range(len(coins[i])):
                up = coins[i-1][j] if i-1 >= 0 else 0
                left = coins[i][j-1] if j-1 >= 0 else 0
                
                if coins[i][j] < 0 and count < 2:
                    coins[i][j] = 0
                    count += 1
                
                coins[i][j] = max(up,left)+coins[i][j]


        return coins[-1][-1]
    

sol = Solution()

print(sol.maximumAmount([[0,1,-1],[1,-2,3],[2,-3,4]]))
print(sol.maximumAmount([[10,10,10],[10,10,10],[10,10,10]]))