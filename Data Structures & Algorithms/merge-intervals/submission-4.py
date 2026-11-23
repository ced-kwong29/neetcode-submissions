class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)

        res = []
        currInterval = intervals[0]
        ndx, end = 1, len(intervals)
        while ndx < end:
            if currInterval[1] >= intervals[ndx][0]:
                currInterval[0] = min(currInterval[0], intervals[ndx][0])
                currInterval[1] = max(currInterval[1], intervals[ndx][1])
            else:
                res.append(currInterval)
                currInterval = intervals[ndx]
            ndx += 1

        return res + [currInterval]