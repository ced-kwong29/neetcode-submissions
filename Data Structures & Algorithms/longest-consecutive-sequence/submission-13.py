class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqLength = defaultdict(int)
        maxLength = 0

        for n in nums:
            if seqLength[n] != 0:
                continue

            seqLength[n] = seqLength[n - 1] + 1 + seqLength[n + 1]
            if seqLength[n] > maxLength:
                maxLength = seqLength[n]

            seqLength[n - seqLength[n - 1]] = seqLength[n]
            seqLength[n + seqLength[n + 1]] = seqLength[n]

        return maxLength