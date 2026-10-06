class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up, down  = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while up <= down:
            rowMid = (up + down) // 2

            if matrix[rowMid][left] <= target <= matrix[rowMid][right]:
                while left <= right:
                    colMid = (left + right) // 2
                    if matrix[rowMid][colMid] == target:
                        return True

                    if matrix[rowMid][colMid] < target:
                        left = colMid + 1
                    else:
                        right = colMid - 1
                return False

            if target < matrix[rowMid][left]:
                down = rowMid - 1
            else:
                up = rowMid + 1
            
        return False