class Solution {
    public int minDistance(String s, String t) {
        int m = s.length(), n = t.length(), prev[] = new int[n+1];
        for(int i = 0; i < n; ++i){
            prev[i] = n - i;
        }

        for(int i = m - 1; i >= 0; --i){
            int[] curr = new int[n+1];
            curr[n] = m - i;

            for(int j = n - 1; j >= 0; --j){
                if(s.charAt(i) == t.charAt(j)){
                    curr[j] = prev[j+1];
                }
                else{
                    curr[j] = 1 + Math.min(prev[j], Math.min(prev[j+1], curr[j+1]));
                }
            }

            prev = curr;
        }

        return prev[0];
    }
}
