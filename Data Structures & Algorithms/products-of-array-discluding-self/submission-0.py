class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref, suff = [1] * (n+2), [1] * (n+2)

        for i in range(n):
            pref[i+1] = pref[i] * nums[i]
            suff[n - i] = suff[n - i + 1] * nums[n - i - 1]
        
        return [p * s for p, s in zip(pref[:-2], suff[2:])]
    