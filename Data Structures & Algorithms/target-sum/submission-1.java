class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        var dp = new HashMap<Integer, Integer>();
        dp.put(0,1);

        for(int i : nums){
            var nextDp = new HashMap<Integer, Integer>();
            for(Map.Entry<Integer,Integer> entry : dp.entrySet()){
                int total = entry.getKey(), count = entry.getValue();
                nextDp.put(total + i, nextDp.getOrDefault(total + i, 0) + count);
                nextDp.put(total - i, nextDp.getOrDefault(total - i, 0) + count);
            }
            dp = nextDp;
        }

        return dp.getOrDefault(target, 0);
    }
}
