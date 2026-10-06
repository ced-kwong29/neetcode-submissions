class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        left, right = 1, len(height) - 2
        maxL, maxR = height[left - 1], height[right + 1]

        while left <= right:
            if maxL < maxR:
                if height[left] > maxL:
                    maxL = height[left]

                water += maxL - height[left]
                left += 1
            else:
                if height[right] > maxR:
                    maxR = height[right]
                
                water += maxR - height[right]
                right -= 1
        
        return water