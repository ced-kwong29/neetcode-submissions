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
        end = len(word)
        def dfs(ndx, node):
            curr = node
            for i in range(ndx, end):
                char = word[i]
                if char == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                
                else:
                    if not curr.children.get(char):
                        return False
                    curr = curr.children[char]

            return curr.end
        
        return dfs(0, self.root)


