class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        for c in t:
            if c in freq:
                if freq[c] > 1:
                    freq[c] -= 1
                else:
                    del freq[c]
            else:
                return False
        
        return not freq