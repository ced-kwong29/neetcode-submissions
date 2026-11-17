class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])

        end = len(word)
        def dfs(r, c, visited, index):
            
            if (r, c) in visited or board[r][c] != word[index]:
                return False

            visited.add((r, c))
            nextIndex = index + 1

            if nextIndex == end:
                return True

            for vert, hori in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
                newR, newC = r + vert, c + hori
                if 0 <= newR < row and 0 <= newC < col and dfs(newR, newC, visited, nextIndex):
                    return True

            visited.remove((r, c))
            return False


        for r in range(row):
            for c in range(col):
                if dfs(r,c, set(), 0):
                    return True

        return False

