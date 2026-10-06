class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0

        seen = dict()
        left, end = 0, len(s)
        for right in range(end):
            if seen.get(s[right], -1) >= left:
                currLength = right - left
                if currLength > maxLength:
                    maxLength = currLength

                left = seen[s[right]] + 1

            seen[s[right]] = right

        return max(maxLength, end - left)

