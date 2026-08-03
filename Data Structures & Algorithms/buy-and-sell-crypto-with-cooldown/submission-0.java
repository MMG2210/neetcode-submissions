class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length, dp[][] = new int[n + 2][2];
        for(int i = n - 1; i >= 0; --i){
            for(int buy = 1; buy >= 0; --buy){
                if(buy == 1){
                    dp[i][buy] = Math.max(dp[i+1][buy], -prices[i] + dp[i+1][1-buy]);
                }
                else{
                    dp[i][buy] = Math.max(dp[i+1][buy], prices[i] + dp[i+2][1-buy]);
                }
            }
        }

        return dp[0][1];
    }
}
