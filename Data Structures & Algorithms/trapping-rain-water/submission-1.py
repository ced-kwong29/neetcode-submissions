class Solution:
    def trap(self, height: List[int]) -> int:
        totalWater = 0

        maxLeft, maxRight = height[0], height[-1]
        left, right = 0, len(height) - 1

        while left < right:
            if maxLeft < maxRight:
                left += 1
                if height[left] > maxLeft:
                    maxLeft = height[left]

                totalWater += maxLeft - height[left]
            else:
                right -= 1
                if height[right] > maxRight:
                    maxRight = height[right]

                totalWater += maxRight - height[right]

        return totalWater
