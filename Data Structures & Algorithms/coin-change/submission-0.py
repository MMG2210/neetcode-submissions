class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10**9] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for val in range(coin, amount+1):
                dp[val] = min(dp[val], 1 + dp[val - coin])
        
        return dp[amount] if dp[amount] < (10**9) else -1
