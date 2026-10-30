class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        smallLength = len(self.small)
        largeLength = len(self.large)

        if smallLength > largeLength + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if largeLength > smallLength + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)


    def findMedian(self) -> float:
        smallLength, largeLength = len(self.small), len(self.large)
        if smallLength > largeLength:
            return -1 * self.small[0]

        if largeLength > smallLength:
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2.0
        