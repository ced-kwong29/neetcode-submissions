class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        count = 0

        for x, y in points:
            heapq.heappush(minHeap, (-(x**2 + y**2), x, y))
            count += 1

            if count > k:
                heapq.heappop(minHeap)

        return [[x,y] for _,x,y in minHeap]