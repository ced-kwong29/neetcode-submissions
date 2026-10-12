class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        end = len(word)

        def dfs(r, c, seen, pos) -> bool:
            if pos == end:
                return True

            if not (0 <= r < row and 0 <= c < col) or (r, c) in seen or board[r][c] != word[pos]:
                return False

            for vert, hori in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
                newR, newC = vert + r, hori + c
                if dfs(newR, newC, seen + [(r,c)], pos + 1):
                    return True

            return False

        for r in range(row):
            for c in range(col):
                if dfs(r, c, [], 0):
                    return True
        
        return False