class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in seen:
                seen[nums[i]] = i
            else:
                return [i, seen[diff]] if i < seen[diff] else [seen[diff], i]
            