class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()

        for s in strs:
            sortedStr = "".join(sorted(s))
            groups[sortedStr] = groups.get(sortedStr, []) + [s]

        return [g for g in groups.values()]