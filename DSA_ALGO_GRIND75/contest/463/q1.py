from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        original_profit = sum(s * p for s, p in zip(strategy, prices))
        max_profit = original_profit

        prefix_prices = [0]
        for price in prices:
            prefix_prices.append(prefix_prices[-1] + price)

        for start in range(n - k + 1):

            old_profit = sum(strategy[i] * prices[i] for i in range(start, start + k))

            new_profit = sum(prices[i] for i in range(start + k // 2, start + k))

            modified_profit = original_profit - old_profit + new_profit
            max_profit = max(max_profit, modified_profit)

        return max_profit