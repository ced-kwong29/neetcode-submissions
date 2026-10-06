class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] < minNum:
                minNum = nums[mid]

            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return minNum