class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        row, col = len(grid), len(grid[0])

        def dfs(x, y):
            grid[x][y] = "0"

            directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
            for vert, hori in directions:
                r, c = vert + x, hori + y
                if 0 <= r < row and 0 <= c < col and grid[r][c] == "1":
                    dfs(r, c)
    
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1

        return count