class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for n in nums:
            seen[n] = seen.get(n, 0) + 1
            if seen[n] > 1:
                return True
        return False
        