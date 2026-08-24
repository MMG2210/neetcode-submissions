class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, freq, res = 0, defaultdict(), 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            mostSeen = max(freq.values())
            while r - l + 1 - mostSeen > k:
                freq[s[l]] -= 1
                mostSeen = max(freq.values())
                l += 1
            res = max(res, r - l + 1)
        return res
