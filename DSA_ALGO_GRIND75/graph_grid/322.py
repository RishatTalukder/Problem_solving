class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # make a recursive function to try out the possibilities

        memo = {}
        def dfs(remaining):
            if remaining == 0:
                return 0
            
            if remaining in memo:
                return memo[remaining]
            
            min_coins = float("inf")
            for coin in coins:
                if remaining - coin >= 0:
                    min_coins = min(min_coins, dfs(remaining - coin) + 1)
            
            memo[remaining] = min_coins
            return min_coins
        
        result = dfs(amount)

        return result if result != float("inf") else -1
    


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # recursive binary decision tree to try out the possibilities
        
        current = []

        def dfs(remaining, index):
            if remaining == 0:
                current.append(0)
                return
            
            if remaining < 0 or index == len(coins):
                return
            
            # include the current coin
            current.append(coins[index])
            dfs(remaining - coins[index], index)
            current.pop()
            
            # exclude the current coin
            dfs(remaining, index + 1)

        dfs(amount, 0)
        return min(current) if current else -1