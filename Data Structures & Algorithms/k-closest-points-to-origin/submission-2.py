class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for p in points:
            x, y = p
            heapq.heappush(minHeap, (-(x**2 + y**2), p))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return [p for _,p in minHeap]