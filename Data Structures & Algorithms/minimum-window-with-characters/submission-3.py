class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        t_count = Counter(t)
        window = {}

        have, need = 0, len(t_count)
        res_len, res_range = float("inf"), (-1,-1)
        l = 0

        for r, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1

            if ch in t_count and window[ch] == t_count[ch]:
                have += 1
            
            while have == need:
                if r - l + 1 < res_len:
                    res_len, res_range = r - l + 1, (l, r)
                window[s[l]] -= 1
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        
        return s[res_range[0]: res_range[1] + 1]