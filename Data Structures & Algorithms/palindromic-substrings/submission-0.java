class Solution {
    public int countSubstrings(String s) {
        int n = s.length(), count = 0;
        boolean dp[][] = new boolean[n][n];

        for(int len = 1; len <= n; ++len){
            for(int i = 0; i <= n - len; ++i){
                int j = i + len - 1;
                if(s.charAt(i) == s.charAt(j)){
                    if(len <= 2 || dp[i + 1][j - 1]){
                        dp[i][j] = true;
                        count++;
                    }
                }
            }
        }

        return count;
    }
}
