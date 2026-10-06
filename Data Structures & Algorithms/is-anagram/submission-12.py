class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lengthS = len(s)
        if lengthS != len(t):
            return False

        freq = defaultdict(int)
        for n in range(lengthS):
            freq[s[n]] += 1
            freq[t[n]] -= 1

        for count in freq.values():
            if count != 0:
                return False
        return True