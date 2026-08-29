class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, skip = 0, 0
        for num in nums:
            prev, skip = skip, max(skip, num + prev)
        return skip