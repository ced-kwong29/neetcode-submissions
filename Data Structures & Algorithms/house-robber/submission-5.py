class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, nums[0]

        for n in nums[1:]:
            tmp = rob2
            rob2 = max(n + rob1, rob2)
            rob1 = tmp

        return rob2