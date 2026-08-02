class Solution {
    private String expand(String s, int start, int end){
        while(start > 0 && end < s.length() - 1){
            if(s.charAt(start - 1) == s.charAt(end + 1)){
                start--;
                end++;
            }
            else break;
        }
        return s.substring(start, end + 1);
    }

    public String longestPalindrome(String s) {
        if(s.length() == 1){
            return s;
        }
        
        String res = "";
        for(int i = 0; i < s.length() - 1; ++i){
            String first = expand(s, i, i), second = (s.charAt(i) == s.charAt(i + 1)? expand(s, i, i + 1) : "");
            if(res.length() < first.length()){
                res = first;
            }
            if(res.length() < second.length()){
                res = second;
            }
        }
        return res;
    }
}
