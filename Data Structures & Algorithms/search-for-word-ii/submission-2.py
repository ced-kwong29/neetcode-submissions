class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False

    def add(self, word) -> None:
        curr = self
        for char in word:
            if not curr.children.get(char):
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.add(w)

        visited, found = set(), set()
        def search(r, c, node, word):
            if (r, c) in visited or not node.children.get(board[r][c]):
                return

            visited.add((r, c))

            word += board[r][c]
            if node.children[board[r][c]].end:
                found.add(word)
                
            for vert, hori in {(1, 0), (-1, 0), (0, -1), (0, 1)}:
                newR, newC = vert + r, hori + c
                if 0 <= newR < row and 0 <= newC < col:
                    search(newR, newC, node.children[board[r][c]], word)

            visited.remove((r, c))

        
        row, col = len(board), len(board[0])
        for r in range(row):
            for c in range(col):
                search(r, c, root, "")

        return list(found)