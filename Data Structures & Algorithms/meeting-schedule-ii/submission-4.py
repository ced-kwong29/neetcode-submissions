"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes = sorted([i.start for i in intervals])
        endTimes = sorted([i.end for i in intervals])

        result, count = 0, 0
        start, end, total = 0, 0, len(intervals)
        while start < total:
            if startTimes[start] < endTimes[end]:
                start += 1
                count += 1
            else:
                end += 1
                count -= 1

            if count > result:
                result = count

        return result

