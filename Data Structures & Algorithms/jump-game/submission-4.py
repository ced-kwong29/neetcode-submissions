class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1
        goal = end
        for i in range(end, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0