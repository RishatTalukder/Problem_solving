class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount%10 >= 5:
            purchaseAmount = purchaseAmount + 10 - purchaseAmount%10
        
        else:
            purchaseAmount = purchaseAmount - purchaseAmount%10

        return 100 - purchaseAmount



sol = Solution()

print(sol.accountBalanceAfterPurchase(11)) # 50