class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []

        end = len(nums)
        def generate(ndx, combo):
            currSum = sum(combo)
            if currSum == target:
                combos.append(combo)
                return

            for i in range(ndx, end):
                if currSum + nums[i] > target:
                    continue
                generate(i, combo + [nums[i]])

        generate(0, [])
        return combos