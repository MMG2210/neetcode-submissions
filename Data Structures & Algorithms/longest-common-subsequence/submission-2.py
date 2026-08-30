class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        """
        if chars are equal
        fn(i,j) = 1 + fn(i-1, j-1)
        else
        fn(i,j) = max(fn(i-1,j), fn(i,j-1))

        in terms of arrays 
        equal case
        dp[j] = 1 + dp[j-1]
        else case
        dp[j] = max(dp[j], dp[j-1])
        """
        if(len(s) < len(t)):
            return self.longestCommonSubsequence(t,s)

        m, n = len(s), len(t)
        dp = [0] * (n+1)

        for i in range(m-1, -1, -1):
            prev = 0
            for j in range(n-1, -1, -1):
                temp = dp[j]
                if s[i] == t[j]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j], dp[j+1])
                prev = temp
        return dp[0]

        