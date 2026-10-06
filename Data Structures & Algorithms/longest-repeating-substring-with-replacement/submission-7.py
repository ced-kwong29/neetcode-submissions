class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowLength = 0

        freq = defaultdict(int)
        maxFreq = 0

        left = 0
        for right in range(len(s)):
            freq[s[right]] += 1
            if freq[s[right]] > maxFreq:
                maxFreq = freq[s[right]]
            
            while (right + 1 - left) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1

            windowLength = right + 1 - left
        
        return windowLength