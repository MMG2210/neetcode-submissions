class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        var wordSet = new HashSet<String>(wordDict);
        int n = s.length();
        boolean dp[] = new boolean[n+1];
        dp[n] = true;

        for(int i = n - 1; i >= 0; --i){
            for(int j = i; j < n; ++j){
                if(wordSet.contains(s.substring(i,j+1)) && dp[j + 1]){
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[0];
    }
}
