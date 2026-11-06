class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        boughtFor = prices[0]
        for p in prices[1:]:
            if p < boughtFor:
                boughtFor = p
            
            currProfit = p - boughtFor
            if currProfit > maxProfit:
                maxProfit = currProfit

        return maxProfit