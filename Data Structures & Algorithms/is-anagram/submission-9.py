class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length = len(s)
        if length != len(t):
            return False

        count = [0] * 26
        for i in range(length):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        return all(v == 0 for v in count)