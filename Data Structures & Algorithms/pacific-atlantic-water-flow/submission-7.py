class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])

        pac, atl = set(), set()
        def dfs(r, c, visited):
            visited.add((r, c))

            for vert, hori in {(1, 0), (-1, 0), (0, -1), (0, 1)}:
                newR, newC = r + vert, c + hori
                if 0 <= newR < row and 0 <= newC < col and (newR, newC) not in visited and heights[r][c] <= heights[newR][newC]:
                    dfs(newR, newC, visited)


        for r in range(row):
            dfs(r, 0, pac)
            dfs(r, col - 1, atl)

        for c in range(col):
            dfs(0, c, pac)
            dfs(row - 1, c, atl)

        return [[r, c] for r in range(row) for c in range(col) if (r, c) in pac and (r, c) in atl]

            