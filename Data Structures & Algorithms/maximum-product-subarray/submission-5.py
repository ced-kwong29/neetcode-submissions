class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        curMax, curMin = 1, 1
        for n in nums:
            maxProd, minProd = curMax * n, curMin * n
            curMax = max(n, maxProd, minProd)
            curMin = min(n, maxProd, minProd)

            if curMax > res:
                res = curMax

        return res