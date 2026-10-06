class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length = len(s)
        if length != len(t):
            return False

        s_freq, t_freq = {}, {}
        for i in range(length):
            s_freq[s[i]] = s_freq.get(s[i], 0) + 1
            t_freq[t[i]] = t_freq.get(t[i], 0) + 1

        return s_freq == t_freq