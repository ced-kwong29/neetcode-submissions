class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0

        freq = defaultdict(int)
        maxFreq = 0

        left, end = 0, len(s)
        for right in range(end):
            freq[s[right]] += 1
            if freq[s[right]] > maxFreq:
                maxFreq = freq[s[right]]

            while right - left + 1 - maxFreq > k:
                freq[s[left]] -= 1
                left += 1
            
            currLength = right - left + 1
            if currLength > maxLength:
                maxLength = currLength

        return maxLength