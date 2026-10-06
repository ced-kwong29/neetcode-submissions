class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longestWindow = 0

        freq = {}
        maxFreq = 0

        left = 0
        for right in range(len(s)):
            freq[s[right]] = 1 + freq.get(s[right], 0)
            if freq[s[right]] > maxFreq:
                maxFreq = freq[s[right]]

            while (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1

            currWindow = right - left + 1
            if currWindow > longestWindow:
                longestWindow = currWindow
        
        return longestWindow
