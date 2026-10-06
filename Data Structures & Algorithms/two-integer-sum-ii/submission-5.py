class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            twoSum = numbers[left] + numbers[right]
            if twoSum == target:
                return [left + 1, right + 1]

            mid = right - (left // 2)

            if twoSum > target:
                right -= 1
            else:
                left += 1
