class Solution {
    Boolean[][] dp;
    int m, n;

    private boolean fn(String s, String t, int i, int j){
        if(j < 0){
            return i < 0;
        }

        if(i < 0){
            return t.charAt(j) == '*' && fn(s, t, i, j-2);
        }

        if(dp[i][j] != null){
            return dp[i][j];
        }
        dp[i][j] = false;
        if(t.charAt(j) == '.' || t.charAt(j) == s.charAt(i)){
            dp[i][j] = fn(s, t, i-1, j-1);
        }
        else if(t.charAt(j) == '*'){
            dp[i][j] = ((t.charAt(j-1) == '.' || t.charAt(j-1) == s.charAt(i)) && fn(s, t, i-1,j)) 
            || fn(s, t, i, j-2);
        }

        return dp[i][j];
    }

    public boolean isMatch(String s, String p) {
        m = s.length();
        n = p.length();
        dp = new Boolean[m][n];
        return fn(s, p, m-1, n-1);
    }
}
