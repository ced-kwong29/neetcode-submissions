class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0

        end = len(s)
        seen = {}

        left, end = 0, len(s)
        for right in range(end):
            char = s[right]
            if seen.get(char) != None and left <= seen[char]:
                currLength = right - left
                if currLength > maxLength:
                    maxLength = currLength

                left = seen[char] + 1

            seen[char] = right

        return max(maxLength, end - left)