class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = dict()

        for n in nums:
            if n in seq:
                continue

            seq[n] = 1

            if n + 1 in seq:
                seq[n] += seq[n + 1]

            if n - 1 in seq:
                seq[n] += seq[n - 1]
            
            lower = n - 1
            while lower in seq:
                seq[lower] = seq[n]
                lower -= 1

            upper = n + 1
            while upper in seq:
                seq[upper] = seq[n]
                upper += 1

        return max(seq.values()) if seq else 0
