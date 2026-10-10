class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0

        prevEnd = float("-inf")
        for start, end in intervals:
            if start >= prevEnd:
                prevEnd = end
            else:
                count += 1
                if end < prevEnd:
                    prevEnd = end

        return count