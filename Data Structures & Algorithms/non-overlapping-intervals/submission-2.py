class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1],-x[0]))
        count = 0

        left, right = float("-inf"), float("-inf")
        for start, end in intervals:
            if right == start:
                right = end
            elif right < start:
                left, right = start, end
            else:
                count += 1

        return count