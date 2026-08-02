class Solution {
    private int robHelper(int[] nums, int start, int end){
        int n = nums.length, prev = nums[start], prevSkip = 0;
        for(int i = start + 1; i <= end; ++i){
            int curr = Math.max(prev, nums[i] + prevSkip);
            prevSkip = prev;
            prev = curr;
        }
        return prev;
    }

    public int rob(int[] nums) {
        int n = nums.length;
        if(n == 1){
            return nums[0];
        }
        return Math.max(robHelper(nums, 0, n - 2), robHelper(nums, 1, n - 1));
    }
}
