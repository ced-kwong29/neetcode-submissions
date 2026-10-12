class Solution:
    def longestPalindrome(self, s: str) -> str:
        end = len(s)
        def expand(left, right):
            while left >= 0 and right < end and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        left, right = 0, 0
        maxLength = 0
        for ndx in range(end):
            l1, r1 = expand(ndx, ndx)
            l2, r2 = expand(ndx, ndx + 1)

            length1 = r1 - l1 + 1
            length2 = r2 - l2 + 1
            currMax = max(length1, length2)
            if currMax > maxLength:
                maxLength = currMax
                left, right = (l1, r1) if currMax == length1 else (l2, r2)

        return s[left:right + 1]     
