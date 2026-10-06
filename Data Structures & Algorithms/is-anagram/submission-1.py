class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = Counter(s)

        for char in t:
            if freq.get(char, 0) == 0:
                return False
            
            freq[char] -= 1
            if freq[char] == 0:
                del freq[char]

        return not freq