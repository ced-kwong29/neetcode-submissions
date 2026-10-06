class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqLength = dict()

        maxLength = 0
        for num in nums:
            if num not in seqLength:
                seqLength[num] = seqLength.get(num - 1, 0) + 1 + seqLength.get(num + 1, 0)

                if num + 1 in seqLength:
                    seqLength[num + seqLength[num + 1]] = seqLength[num]

                if num - 1 in seqLength:
                    seqLength[num - seqLength[num - 1]] = seqLength[num]

                if seqLength[num] > maxLength:
                    maxLength = seqLength[num]

        return maxLength