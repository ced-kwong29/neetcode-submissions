class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        maxLength = 0

        seqLength = {}
        for n in nums:
            if n in seqLength:
                continue

            currLength = 1 + seqLength.get(n - 1, 0)
            if currLength > maxLength:
                maxLength = currLength

            seqLength[n] = currLength
        
        return maxLength

            