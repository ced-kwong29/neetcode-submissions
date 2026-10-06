class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        seqLengths = dict()

        for n in nums:
            if seqLengths.get(n):
                continue

            lower, upper = seqLengths.get(n - 1, 0), seqLengths.get(n + 1, 0)
            seqLengths[n] = lower + 1 + upper
            if seqLengths[n] > maxLength:
                maxLength = seqLengths[n]

            if lower > 0:
                seqLengths[n - lower] = seqLengths[n]
            if upper > 0:
                seqLengths[n + upper] = seqLengths[n]

        return maxLength