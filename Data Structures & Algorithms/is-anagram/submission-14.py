class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLength = len(s)
        if sLength != len(t):
            return False

        freq = defaultdict(int)
        for i in range(sLength):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1

        for f in freq:
            if freq[f] != 0:
                return False
        return True
