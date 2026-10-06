class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqLength = dict()

        maxLength = 0
        for num in nums:
            if num not in seqLength:
                currLength = 1 + seqLength.get(num - 1, 0)

                if num + 1 in seqLength:
                    currLength += seqLength[num + seqLength[num + 1]] 
                    seqLength[num + seqLength[num + 1]] = currLength

                if num - 1 in seqLength:
                    seqLength[num - seqLength[num - 1]] = currLength

                seqLength[num] = currLength
                if currLength > maxLength:
                    maxLength = currLength

        return maxLength