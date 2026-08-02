class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length, dp[] = new int[n];

        for(int i = 0; i < n; ++i){
            dp[i] = 1;
            for(int j = i - 1; j >= 0; --j){
                if(nums[j] < nums[i] && dp[i] < 1 + dp[j]){
                    dp[i] = 1 + dp[j];
                }
            }
        }

        return Arrays.stream(dp).max().getAsInt();
    }
}
