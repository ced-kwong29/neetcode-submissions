class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = nums[0]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] < minVal:
                minVal = nums[mid]
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
        return minVal