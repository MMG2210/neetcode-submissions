class Solution {
    public int maxProduct(int[] nums) {
        int INF = (int)(1e9), res = -INF, runMax = 1, runMin = 1;
        for(int i = 0; i < nums.length; ++i){
            runMax *= nums[i];
            runMin *= nums[i];

            if(runMin > runMax){
                int temp = runMin;
                runMin = runMax;
                runMax = temp;
            }

            res = Math.max(res, runMax);
            if(runMax <= 0){
                runMax = 1;
            }

            if(runMin == 0){
                runMin = 1;
            }
        }
        return res;
    }
}
