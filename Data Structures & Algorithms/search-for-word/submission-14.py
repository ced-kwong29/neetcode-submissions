class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        end = len(word)

        def dfs(r, c, pos) -> bool:
            if board[r][c] == '#' or board[r][c] != word[pos]:
                return False
            
            updatedPos = pos + 1
            if updatedPos == end:
                return True

            board[r][c] = '#'
            for vert, hori in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
                newR, newC = vert + r, hori + c
                if 0 <= newR < row and 0 <= newC < col and dfs(newR, newC, updatedPos):
                    return True
            board[r][c] = word[pos]

            return False

        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        
        return False