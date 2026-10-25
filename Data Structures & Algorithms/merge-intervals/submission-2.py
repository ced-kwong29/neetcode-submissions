class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        curr = None
        for i in intervals:
            if not curr:
                curr = i
                continue

            if curr[1] < i[0]:
                res.append(curr)
                curr = i
            else:
                # curr[0] = min(curr[0], i[0])
                curr[1] = max(curr[1], i[1])

        return res + [curr]