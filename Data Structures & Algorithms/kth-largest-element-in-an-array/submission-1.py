class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        count = 0

        for n in nums:
            heapq.heappush(minHeap, n)
            count += 1

            if count > k:
                heapq.heappop(minHeap)

        return minHeap[0]