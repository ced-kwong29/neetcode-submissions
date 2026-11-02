class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        match = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if match.get(diff) != None:
                return [match[diff], i]

            match[nums[i]] = i