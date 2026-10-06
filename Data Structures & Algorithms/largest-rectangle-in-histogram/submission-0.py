class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        end = len(heights)

        stack = []
        for i in range(end):
            start = i
            while stack and stack[-1][1] > heights[i]:
                ndx, h = stack.pop()

                area = h * (i - ndx)
                if area > maxArea:
                    maxArea = area

                start = ndx
        
            stack.append((start, heights[i]))

        for ndx, height in stack:
            area = height * (end - ndx)
            if area > maxArea:
                maxArea = area

        return maxArea

