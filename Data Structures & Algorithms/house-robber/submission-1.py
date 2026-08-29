class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        
        prev, skip = max(nums[1],nums[0]), nums[0]
        for i in range(2, len(nums)):
            cur = max(prev, nums[i] + skip)
            skip = prev
            prev = cur
        
        return prev