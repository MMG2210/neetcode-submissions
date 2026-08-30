class Solution:
    def expand_string(self, s: str, l: int, r: int) -> tuple[int, int]:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l+1, r

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        start, end = 0, 0
        for i in range(len(s)):
            l1, r1 = self.expand_string(s, i, i)
            if (r1 - l1) > (end - start):
                start, end = l1, r1
            
            l2, r2 = self.expand_string(s, i, i+1)
            if (r2 - l2) > (end - start):
                start, end = l2, r2

        return s[start:end]