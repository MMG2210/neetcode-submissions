class Solution:
    def rob_helper(self, nums: list) -> int:
        prev, skip = 0, 0
        for num in nums:
            skip, prev = prev, max(prev, skip + num)
        return prev
    
    def rob(self, nums: List[int]) -> int:
        return max(self.rob_helper(nums[:-1]), self.rob_helper(nums[1:])) if len(nums) > 1 else nums[0]