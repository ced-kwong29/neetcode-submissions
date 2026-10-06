class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqLength = dict()
        maxLength = 0

        for n in nums:
            if n in seqLength:
                continue
                
            lower = seqLength.get(n - 1, 0)
            upper = seqLength.get(n + 1, 0)

            seqLength[n] = lower + 1 + upper
            if seqLength[n] > maxLength:
                maxLength = seqLength[n]

            if lower > 0:
                seqLength[n - seqLength[n - 1]] = seqLength[n]
            if upper > 0:
                seqLength[n + seqLength[n + 1]] = seqLength[n]

        return maxLength