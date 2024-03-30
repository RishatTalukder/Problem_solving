class Solution:
    def maximumWealth(self, accounts):
        length = len(accounts)
        return_max = [0]*length
        for ind,val in enumerate(accounts):
            summ = sum(val)
            return_max[ind] = summ 
        
        return max(return_max)
        

accounts =  [[2,8,7],[7,1,3],[1,9,5]]

print(Solution().maximumWealth(accounts))