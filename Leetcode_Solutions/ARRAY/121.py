class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell
        
        return profit
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = prices[0]

        for price in prices:
            if price <= buy:
                buy = price

            else:
                ans = max(ans, price-buy)

        return ans