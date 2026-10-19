class Solution:
    def rob(self, nums: List[int]) -> int:
        prevAmount, maxAmount = 0, 0

        for n in nums:
            newMax = max(prevAmount + n, maxAmount)
            prevAmount = maxAmount
            maxAmount = newMax

        return maxAmount