class Solution {
    public int coinChange(int[] coins, int amount) {
        int n = coins.length, dp[] = new int[amount + 1], INF = (int)(1e9);
        Arrays.fill(dp, INF);
        dp[0] = 0;

        for(int i = 0; i < n; ++i){
            for(int j = coins[i]; j <= amount; ++j){
                dp[j] = Math.min(dp[j], 1 + dp[j - coins[i]]);
            }
        }
        return dp[amount] == INF? -1 : dp[amount];
    }
}
