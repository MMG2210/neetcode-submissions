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

        m, n = len(s), len(t)
        prev = [0] * (n+1)

        for i in range(1, m+1):
            cur = [0] * (n+1)
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    cur[j] = 1 + prev[j-1]
                else:
                    cur[j] = max(cur[j-1], prev[j])
            prev = cur
        return prev[n]

        