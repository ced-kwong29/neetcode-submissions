class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1

            key = tuple(freq)
            if groups.get(key):
                groups[key].append(s)
            else:
                groups[key] = [s]

        return list(groups.values())