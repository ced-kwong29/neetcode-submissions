class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])

        pac = set()
        atl = set()
        def dfs(r, c, visit):
            visit.add((r, c))

            for vert, hori in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
                newR, newC = vert + r, hori + c
                if 0 <= newR < row and 0 <= newC < col and (newR, newC) not in visit and heights[newR][newC] >= heights[r][c]:
                    dfs(newR, newC, visit)

        for c in range(col):
            dfs(0, c, pac)
            dfs(row - 1, c, atl)
            
        for r in range(row):
            dfs(r, 0, pac)
            dfs(r, col - 1, atl)

        return [[r,c] for r in range(row) for c in range(col) if (r, c) in pac and (r, c) in atl]