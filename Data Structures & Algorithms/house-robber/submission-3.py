class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, skip = 0, 0
        for num in nums:
            skip, prev = prev, max(prev, num + skip)
        return prev