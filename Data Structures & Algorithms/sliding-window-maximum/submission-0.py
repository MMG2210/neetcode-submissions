class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap, output = [], []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output