class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqLength = defaultdict(int)

        maxLength = 0
        for num in nums:
            if not seqLength[num]:
                seqLength[num] = seqLength[num - 1] + 1 + seqLength[num + 1]

                seqLength[num + seqLength[num + 1]] = seqLength[num]
                seqLength[num - seqLength[num - 1]] = seqLength[num]

                if seqLength[num] > maxLength:
                    maxLength = seqLength[num]

        return maxLength