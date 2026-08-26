class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low <= high:
            mid, timeNeeded = (high + low)//2, 0

            for i, pile in enumerate(piles):
                timeNeeded += math.ceil(pile/mid)
            
            if timeNeeded <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low
