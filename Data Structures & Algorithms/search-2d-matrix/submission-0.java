class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        for (int r = 0; r < matrix.length; r++) {
            int left = 0, right = matrix[0].length - 1;
            if (matrix[r][left] <= target && target <= matrix[r][right]) {
                while (left <= right) {
                    int mid = (right + left) / 2;
                    if (matrix[r][mid] == target) {
                        return true;
                    }
                    if (matrix[r][mid] < target) {
                        left = mid + 1;
                    } else {
                        right = mid - 1;
                    }
                }
            }
        }

        return false;
    }
}
