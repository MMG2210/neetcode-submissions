class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low <= high:
            mid = (high + low)//2
            if sum((pile + mid - 1)//mid for pile in piles) <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low
