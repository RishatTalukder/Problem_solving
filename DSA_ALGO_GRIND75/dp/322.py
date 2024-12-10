class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coin = [float("inf")]*(amount+1)
        min_coin[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                min_coin[i] = min(min_coin[i], min_coin[i-coin]+1)

        return min_coin[-1] if min_coin[-1] == float("inf") else -1