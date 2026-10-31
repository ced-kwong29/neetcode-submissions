class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def add(self, word):
        cur = self
        for char in word:
            if not cur.children.get(char):
                cur.children[char] = TrieNode()
            cur = cur.children[char]

        cur.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add(word)

        row, col = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if (r, c) in visited or not node.children.get(board[r][c]):
                return

            visited.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)

            for vert, hori in {(1, 0), (-1, 0), (0, -1), (0, 1)}:
                newR, newC = vert + r, hori + c
                if 0 <= newR < row and 0 <= newC < col:
                    dfs(newR, newC, node, word)
            
            visited.remove((r, c))
            
        for r in range(row):
            for c in range(col):
                dfs(r, c, root, "")

        return list(res)