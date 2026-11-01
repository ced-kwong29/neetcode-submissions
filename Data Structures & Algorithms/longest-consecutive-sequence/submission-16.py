class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        seqLength = defaultdict(int)

        for n in nums:
            if seqLength.get(n):
                continue

            left, right = seqLength.get(n - 1, 0), seqLength.get(n + 1, 0)

            seqLength[n] = left + 1 + right
            if seqLength[n] > maxLength:
                maxLength = seqLength[n]

            if left:
                seqLength[n - left] = seqLength[n]
            if right:
                seqLength[n + right] = seqLength[n]

        return maxLength
