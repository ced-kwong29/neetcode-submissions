class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []
        end = len(nums)

        def generateCombo(combo, ndx, total):
            if total == target:
                combos.append(combo)
                return

            for i in range(ndx, end):
                if total + nums[i] > target:
                    continue
                generateCombo(combo + [nums[i]], i, total + nums[i])

        generateCombo([], 0, 0)
        return combos