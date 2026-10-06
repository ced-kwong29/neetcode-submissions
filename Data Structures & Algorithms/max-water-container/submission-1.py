class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        left, right = 0, len(heights) - 1
        while left < right:
            distance = right - left
            if heights[left] < heights[right]:
                currArea = heights[left] * (right - left)
                if currArea > maxArea:
                    maxArea = currArea
                left += 1
            else:
                currArea = heights[right] * (right - left)
                if currArea > maxArea:
                    maxArea = currArea
                right -= 1
        
        return maxArea