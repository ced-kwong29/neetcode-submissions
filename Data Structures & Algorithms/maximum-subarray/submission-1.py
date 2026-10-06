class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, maxSum = 0, float("-inf")

        for n in nums:
            if currSum < 0:
                currSum = 0

            currSum += n
            if currSum > maxSum:
                maxSum = currSum

        return maxSum