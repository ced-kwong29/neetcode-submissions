class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLength = len(matrix[0])

        for row in range(len(matrix)):
            if matrix[row][0] <= target <= matrix[row][rowLength - 1]:
                for col in range(rowLength):
                    if matrix[row][col] == target:
                        return True
                return False

        return False