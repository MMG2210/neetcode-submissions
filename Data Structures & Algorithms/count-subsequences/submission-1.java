class Solution {
    public int numDistinct(String s, String t) {
        int m = s.length(), n = t.length();
        int[] dp = new int[n+1];
        dp[0] = 1;

        for(int i = 1; i <= m; ++i){
            for(int j = n; j >= 1; --j){
                dp[j] += (s.charAt(i-1) == t.charAt(j-1)? dp[j-1] : 0);
            }
        }

        return dp[n];
    }
}
