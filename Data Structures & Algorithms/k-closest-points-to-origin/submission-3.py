class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        count = 0

        for p in points:
            x, y = p
            heapq.heappush(minHeap, (-(x**2 + y**2), p))
            count += 1
            if count > k:
                heapq.heappop(minHeap)

        return [p for _,p in minHeap]