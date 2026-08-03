class Solution {
    public int longestCommonSubsequence(String s, String t) {
        if(s.length() < t.length()){
            return longestCommonSubsequence(t,s);
        }

        int m = s.length(), n = t.length(), dp[] = new int[n+1];
        dp[n] = 0;

        for(int i = m - 1; i >= 0; --i){
            int prev = 0;
            for(int j = n - 1; j >= 0; --j){
                int temp = dp[j];
                if(s.charAt(i) == t.charAt(j)){
                    dp[j] = 1 + prev;
                }
                else{
                    dp[j] = Math.max(dp[j], dp[j+1]);
                }
                prev = temp;
            }
        }
        return dp[0];
    }
}


/*

i : m-1 -> 0
j : n-1 -> 0
case 1: s[i] == t[j] :-
    T[i][j] = 1 + T[i+1][j+1]
case 2: s[i] != t[j] :-
    T[i][j] = Math.max(T[i+1][j], T[i][j+1])

*/
