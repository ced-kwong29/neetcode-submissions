class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by start
        # track current interval
        # update the end of interval with every overlapping interval
        # add to final result move on to next interval
        intervals.sort()

        res = []
        currInterval = intervals[0][:]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= currInterval[1]:
                currInterval[0] = min(intervals[i][0], currInterval[0])
                currInterval[1] = max(intervals[i][1], currInterval[1])
            else:
                res.append(currInterval)
                currInterval = intervals[i][:]

        return res + [currInterval]
                