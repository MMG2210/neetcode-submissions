class Solution {
    public int maxCoins(int[] nums) {
        int n = nums.length, dp[][] = new int[n+2][n+2], arr[] = new int[n+2];
        Arrays.fill(arr, 1);
        for(int i = 0; i < n; ++i)arr[i+1] = nums[i];
        for(int j = 1; j <= n; ++j){
            dp[0][j] = arr[j];
        }

        for(int len = 1; len <= n; ++len){
            for(int i = 1; i <= n - len + 1; ++i){
                int j = i + len - 1;

                for(int k = i; k <= j; ++k){
                    int coins = arr[i-1] * arr[k] * arr[j+1];
                    dp[i][j] = Math.max(dp[i][j], coins + dp[i][k-1] + dp[k+1][j]);
                }
            }
        }

        return dp[1][n];
    }
}
