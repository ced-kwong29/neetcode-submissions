class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        end = len(nums)
        LIS = [1] * end

        for i in range(end - 1, -1, -1):
            for j in range(i + 1, end):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)