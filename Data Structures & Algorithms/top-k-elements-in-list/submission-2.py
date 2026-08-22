class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [item[0] for item in sorted(Counter(nums).items(), key = lambda x : -x[1])[:k]]
        