class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        var dp = new HashMap<Integer, Integer>();
        dp.put(0,1);

        for(int i : nums){
            var nextDp = new HashMap<Integer, Integer>();
            dp.forEach((total, count) -> {
                nextDp.merge(total + i, count, Integer::sum);
                nextDp.merge(total - i, count, Integer::sum);
            });
            dp = nextDp;
        }

        return dp.getOrDefault(target, 0);
    }
}
