class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0

        mapping = dict()
        end = len(s)
        left = 0
        for right in range(end):
            if s[right] in mapping and mapping[s[right]] >= left:
                currLength = right - left
                if currLength > maxLength:
                    maxLength = currLength

                left = mapping[s[right]] + 1

            mapping[s[right]] = right

        return max(maxLength, end - left)