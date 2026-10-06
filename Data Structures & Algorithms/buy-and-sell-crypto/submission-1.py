class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPurchase = float("inf")

        for p in prices:
            if p < minPurchase:
                minPurchase = p
                continue

            profit = p - minPurchase
            if profit > maxProfit:
                maxProfit = profit

        return maxProfit

