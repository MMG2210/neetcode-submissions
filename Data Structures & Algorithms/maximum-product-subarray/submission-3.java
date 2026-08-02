class Solution {
    public int maxProduct(int[] nums) {
        int runMax = nums[0], runMin = nums[0], res = nums[0];

        for(int i = 1; i < nums.length; ++i){
            int curr = nums[i], tempMax = runMax;
            runMax = Math.max(curr, Math.max(curr * runMax, curr * runMin));
            runMin = Math.min(curr, Math.min(curr * tempMax, curr * runMin));
            res = Math.max(res, runMax);
        }
        return res;
    }
}
