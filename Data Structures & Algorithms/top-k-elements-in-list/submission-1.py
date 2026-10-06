class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        pq = [(-freq[n], n) for n in freq]
        heapq.heapify(pq)

        return [heapq.heappop(pq)[1] for _ in range(k)]