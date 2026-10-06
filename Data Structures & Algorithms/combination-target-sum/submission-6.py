class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []
        end = len(nums)

        def generateCombo(combo, ndx):
            comboSum = sum(combo)
            if comboSum == target:
                combos.append(combo)
                return

            for i in range(ndx, end):
                if comboSum + nums[i] > target:
                    continue
                generateCombo(combo + [nums[i]], i)

        generateCombo([], 0)
        return combos