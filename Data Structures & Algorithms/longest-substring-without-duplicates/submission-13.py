class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0

        indices = dict()

        left, end = 0, len(s)
        for right in range(end):
            if indices.get(s[right], -1) >= left:
                currLength = right - left
                if currLength > maxLength:
                    maxLength = currLength

                left = indices[s[right]] + 1
            
            indices[s[right]] = right

        return max(maxLength, end - left)