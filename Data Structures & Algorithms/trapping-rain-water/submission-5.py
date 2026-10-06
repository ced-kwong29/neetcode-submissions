class Solution:
    def trap(self, height: List[int]) -> int:
        totalWater = 0

        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]

        while left <= right:
            if maxLeft < maxRight:
                if height[left] > maxLeft:
                    maxLeft = height[left]

                totalWater += maxLeft - height[left]
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                
                totalWater += maxRight - height[right]
                right -= 1

        return totalWater
