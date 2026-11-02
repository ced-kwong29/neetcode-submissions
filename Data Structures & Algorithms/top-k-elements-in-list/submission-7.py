class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        res = []
        remaining = k

        buckets = [b for b in buckets if b]
        ndx = len(buckets) - 1
        while ndx >= 0 and remaining > 0:
            if buckets[ndx]:
                for i in range(len(buckets[ndx]) - 1, -1, -1):
                    res.append(buckets[ndx][i])

                    remaining -= 1
                    if remaining == 0:
                        break

            ndx -=1

        return res
            






        
