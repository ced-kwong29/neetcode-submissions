class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not curr.children.get(char):
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True
        

    def search(self, word: str) -> bool:
        def dfs(word, node):
            curr = node
            for i, char in enumerate(word):
                if char == ".":
                    for child in curr.children.values():
                        if dfs(word[i + 1:], child):
                            return True
                    return False
                
                else:
                    if not curr.children.get(char):
                        return False

                    curr = curr.children[char]

            return curr.end
        
        return dfs(word, self.root)


