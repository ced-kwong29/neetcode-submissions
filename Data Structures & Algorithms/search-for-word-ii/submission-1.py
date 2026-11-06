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
            if (r, c) in visited:
                return

            visited.add((r, c))
            curr = node
            for char in curr.children:
                if board[r][c] != char:
                    continue

                if curr.children[char].end:
                    found.add(word + char)
                
                for vert, hori in {(1, 0), (-1, 0), (0, -1), (0, 1)}:
                    newR, newC = vert + r, hori + c
                    if 0 <= newR < row and 0 <= newC < col:
                        search(newR, newC, curr.children[char], word + char)

            visited.remove((r, c))

        
        row, col = len(board), len(board[0])
        for r in range(row):
            for c in range(col):
                search(r, c, root, "")

        return list(found)