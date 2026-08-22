class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, val in enumerate(nums):
            if target - val in map:
                return [map.get(target - val), i]
            map[val] = i

        return [0,0]