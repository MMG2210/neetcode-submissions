class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefMax, suffMax, output = [0] * n, [0] * n, [0] * (n - k + 1)

        prefMax[0] = nums[0]
        suffMax[n-1] = nums[n-1]

        for i in range(1,n):
            if i % k == 0:
                prefMax[i] = nums[i]
            else:
                prefMax[i] = max(prefMax[i-1], nums[i])
            
            if (n-1-i) % k == 0:
                suffMax[n - 1 - i] = nums[n-1-i]
            else:
                suffMax[n-1-i] = max(suffMax[n-i], nums[n-i-1])
        
        for i in range(n - k + 1):
            output[i] = max(prefMax[i + k - 1], suffMax[i])
        return output