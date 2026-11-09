class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd, minProd = max(nums), min(nums)

        curMax, curMin = 1, 1
        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1

            tmp = curMax * n
            curMax = max(n, tmp, curMin * n)
            curMin = min(n, tmp, curMin * n)

            if curMax > maxProd:
                maxProd = curMax

        return maxProd