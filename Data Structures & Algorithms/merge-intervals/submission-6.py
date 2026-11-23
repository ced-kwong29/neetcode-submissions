class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]
        ndx = 0

        for i in range(1, len(intervals)):
            if res[ndx][1] >= intervals[i][0]:
                res[ndx][0] = min(res[ndx][0], intervals[i][0])
                res[ndx][1] = max(res[ndx][1], intervals[i][1])
            else:
                res.append(intervals[i])
                ndx += 1

        return res