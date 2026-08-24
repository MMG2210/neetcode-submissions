class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, minCost = 0, 1e9
        for price in prices:
            if minCost > price:
                minCost = price
                continue
            res = max(res, price - minCost)
        return res