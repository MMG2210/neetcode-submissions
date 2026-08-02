class Solution {
    private int robHelper(int[] nums, int start, int end){
        int n = nums.length, dp[] = new int[n];
        dp[start] = nums[start];
        for(int i = start + 1; i <= end; ++i){
            dp[i] = Math.max(dp[i - 1], nums[i] + (i > start + 1? dp[i - 2] : 0));
        }
        return dp[end];
    }

    public int rob(int[] nums) {
        int n = nums.length;
        if(n == 1){
            return nums[0];
        }
        return Math.max(robHelper(nums, 0, n - 2), robHelper(nums, 1, n - 1));
    }
}
