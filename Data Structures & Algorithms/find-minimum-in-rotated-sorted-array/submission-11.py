class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < minimum:
                minimum = nums[mid]

            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return minimum