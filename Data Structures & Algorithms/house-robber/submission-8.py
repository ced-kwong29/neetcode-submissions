class Solution:
    def rob(self, nums: List[int]) -> int:
        end = len(nums)
        if end <= 2:
            return max(nums)

        rob1, rob2 = nums[0], max(nums[0], nums[1])
        for i in range(2, end):
            rob1, rob2 = rob2, max(nums[i] + rob1, rob2)

        return rob2
