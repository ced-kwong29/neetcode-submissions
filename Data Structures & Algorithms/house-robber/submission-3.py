class Solution:
    def rob(self, nums: List[int]) -> int:
        end = len(nums)
        if end <= 2:
            return max(nums)

        maxAmount = max(nums[0], nums[1])
        dp = [nums[0], maxAmount]

        for i in range(2, end):
            dp.append(max(dp[i - 2] + nums[i], maxAmount))
            if dp[i] > maxAmount:
                maxAmount = dp[i]
            print(dp)

        return maxAmount