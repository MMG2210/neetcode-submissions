class Solution {
    public int countSubstrings(String s) {
        int n = s.length(), count = 0;
        boolean dp[][] = new boolean[n+1][n+1];
    
        for(int i = n - 1; i >= 0; --i){
            for(int j = i; j < n; ++j){
                if(i == j){
                    dp[i][j] = true;
                }

                else if(j == i + 1){
                    dp[i][j] = (s.charAt(i) == s.charAt(j));
                }

                else{
                    dp[i][j] = (s.charAt(i) == s.charAt(j)) && dp[i + 1][j - 1];
                }
            }
        }

        for(int i = 0; i < n; ++i){
            for(int j = 0; j < n; ++j){
                count += (dp[i][j]? 1 : 0);
            }
        }
        return count;
    }
}
