class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = []

        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        for num, count in freq.items():
            heapq.heappush(topK, (count, num))
            if len(topK) > k:
                heapq.heappop(topK)

        return [n for _, n in topK]
