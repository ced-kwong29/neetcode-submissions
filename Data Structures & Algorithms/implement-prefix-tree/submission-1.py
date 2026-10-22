class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if not curr.children.get(char):
                curr.children[char] = TrieNode()

            curr = curr.children[char]
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if not curr.children.get(char):
                return False
            
            curr = curr.children[char]

        return curr.end


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if not curr.children.get(char):
                return False

            curr = curr.children[char]

        return True
