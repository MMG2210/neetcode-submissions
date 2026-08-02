class Solution {
    public boolean canPartition(int[] nums) {
        int n = nums.length, total = Arrays.stream(nums).sum();
        if(total % 2 == 1){
            return false;
        }

        total /= 2;
        boolean dp[] = new boolean[total + 1];
        dp[0] = true;
        for(int i = 0; i < n; ++i){
            for(int j = total; j >= nums[i]; --j){
                if(dp[j - nums[i]]){
                    dp[j] = true;
                }
            }
        }

        return dp[total];
    }
}
