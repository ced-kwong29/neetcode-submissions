class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1],-x[0]))
        print(intervals)
        count = 0

        left, right = intervals[0]
        for start, end in intervals[1:]:
            if right == start:
                right = end
            elif right < start:
                left, right = start, end
            else:
                count += 1

        return count