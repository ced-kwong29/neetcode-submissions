class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        groups = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for i in range(len(s)):
                freq[ord(s[i]) - ord('a')] += 1
            groups[tuple(freq)].append(s)

        return list(groups.values())