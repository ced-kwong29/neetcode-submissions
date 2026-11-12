class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])

        pac, atl = set(), set()
        def dfs(r, c, visited):
            visited.add((r, c))

            for vert, hori in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
                newR, newC = vert + r, hori + c
                if 0 <= newR < row and 0 <= newC < col and (newR, newC) not in visited and heights[newR][newC] >= heights[r][c]:
                    dfs(newR, newC, visited)

        for r in range(row):
            dfs(r, 0, atl)
            dfs(r, col - 1, pac)
        
        for c in range(col):
            dfs(0, c, atl)
            dfs(row - 1, c, pac)

        return [[r, c] for r in range(row) for c in range(col) if (r, c) in pac and (r, c) in atl]