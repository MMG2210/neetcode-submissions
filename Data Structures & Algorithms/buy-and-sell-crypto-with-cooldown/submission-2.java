/*

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

*/


class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length, next[] = new int[2], skip[] = new int[2];
        for(int i = n-1; i >= 0; --i){
            int[] curr = new int[2];
            //1 implies can buy
            curr[1] = Math.max(next[1], -prices[i] + next[0]);
            curr[0] = Math.max(next[0], prices[i] + skip[1]);

            skip = next;
            next = curr;
        }
        return next[1];
    }
}
