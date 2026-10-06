class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ndx, end = 0, len(intervals)

        while ndx < end and intervals[ndx][1] < newInterval[0]:
            ndx += 1
        res = intervals[:ndx]

        while ndx < end and intervals[ndx][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[ndx][0])
            newInterval[1] = max(newInterval[1], intervals[ndx][1])
            ndx += 1

        return res + [newInterval] + intervals[ndx:]


