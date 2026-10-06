class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            sortedStr = "".join(sorted(s))
            if sortedStr not in groups:
                groups[sortedStr] = [s]
            else:
                groups[sortedStr].append(s)

        return [g for g in groups.values()]