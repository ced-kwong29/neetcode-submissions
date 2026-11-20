class Solution:
    def rob(self, nums: List[int]) -> int:
        end = len(nums)
        if end <= 2:
            return max(nums)

        rob1, rob2 = 0, nums[0]
        for i in range(1, end):
            rob1, rob2 = rob2, max(nums[i] + rob1, rob2)

        return rob2
