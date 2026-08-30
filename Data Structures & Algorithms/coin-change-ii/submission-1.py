class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for val in range(coin, amount+1):
                #
                # t[i][j] = t[i-1][j] + t[i][j - coin] ie unbounded knapsack
                # since we are only going to have one array, we have to compute this from coin -> amount
                #
                dp[val] += dp[val - coin]

        return dp[amount]