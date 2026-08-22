class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for val in strs:
            anagram_map["".join(sorted(val))].append(val)

        return list(anagram_map.values())