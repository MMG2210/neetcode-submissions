class Solution {
    public int climbStairs(int n) {
        int oneStepBack = 1, twoStepsBack = 1;
        for(int i = 2; i <= n; ++i){
            int curr = oneStepBack + twoStepsBack;
            twoStepsBack = oneStepBack;
            oneStepBack = curr;
        }

        return oneStepBack;
    }
}
