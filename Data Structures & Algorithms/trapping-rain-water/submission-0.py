class Solution:
    def trap(self, height: List[int]) -> int:
        totalWater = 0

        maxLeft, maxRight = height[0], height[-1]
        left, right = 0, len(height) - 1

        while left <= right:
            if maxLeft < maxRight:
                totalWater += max(0, maxLeft - height[left])
                if height[left] > maxLeft:
                    maxLeft = height[left]

                left += 1
            else:
                totalWater += max(0, maxRight - height[right])
                if height[right] > maxRight:
                    maxRight = height[right]

                right -= 1

        return totalWater
