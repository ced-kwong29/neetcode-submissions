class Solution:
    def longestPalindrome(self, s: str) -> str:
        end = len(s)
        def expand(left, right):
            while left >= 0 and right < end and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        longestPalindrome = ""
        maxLength = 0
        for ndx in range(end):
            l1, r1 = expand(ndx, ndx)
            l2, r2 = expand(ndx, ndx + 1)

            length1 = r1 - l1 + 1
            length2 = r2 - l2 + 1
            currMax = max(length1, length2)
            if currMax > maxLength:
                maxLength = currMax
                longestPalindrome = s[l1:r1 + 1] if currMax == length1 else s[l2:r2 + 1]

        return longestPalindrome     
