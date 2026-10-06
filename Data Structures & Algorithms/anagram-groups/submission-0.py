class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = []

        group_freq = {}
        group_num = 0

        for s in strs:
            char_freq = Counter(s)
            
            g = 0
            while g < group_num and char_freq != group_freq[g]:
                g += 1
            
            if g == group_num:
                sublists.append([s])
                group_freq[group_num] = char_freq
                group_num += 1
            else:
                sublists[g].append(s)

        return sublists