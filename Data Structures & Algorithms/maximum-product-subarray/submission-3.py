class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:
            maxProd, minProd = curMax * n, curMin * n
            curMax = max(maxProd, minProd, n)
            curMin = min(maxProd, minProd, n)
            res = max(res, curMax)

        return res