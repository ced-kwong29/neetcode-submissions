class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            group = tuple(sorted(s))
            groups[group].append(s)

        return list(groups.values())