class Solution {
    public int maxArea(int[] heights) {
        int maxArea = 0;

        int left = 0, right = heights.length - 1;
        while (left < right) {
            int distance = right - left;
            int shorterWall;
            if (heights[left] < heights[right]) {
                shorterWall = heights[left++];
            } else {
                shorterWall = heights[right--];
            }
            maxArea = Math.max(maxArea, distance * shorterWall);
        }

        return maxArea;
    }
}
