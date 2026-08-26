class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqOrig = {}
        for ch in s1:
            freqOrig[ch] = freqOrig.get(ch, 0) + 1
        print(freqOrig)

        for j in range(len(s2)):
            k = j
            freq = dict(freqOrig)

            while len(freq) > 0 and k < len(s2) and s2[k] in freq:
                freq[s2[k]] = freq.get(s2[k]) - 1
                if freq[s2[k]] == 0:
                    freq.pop(s2[k])
                if len(freq) == 0:
                    return True
                k+=1

            j = k
        
        return False
        