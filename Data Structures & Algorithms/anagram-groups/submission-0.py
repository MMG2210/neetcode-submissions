class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for val in strs:
            key = "".join(sorted(val))
            if key not in anagram_map:
                anagram_map[key] = []
            anagram_map.get(key).append(val)

        return list(anagram_map.values())