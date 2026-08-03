class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length, buyLater = 0, sellLater = 0, buyAfterCooldown = 0;

        for(int i = n - 1; i >= 0; --i){
            int buyNow = Math.max(buyLater, -prices[i] + sellLater);
            int sellNow = Math.max(sellLater, prices[i] + buyAfterCooldown);

            buyAfterCooldown = buyLater;
            buyLater = buyNow;
            sellLater = sellNow;
        }

        return buyLater;
    }
}
