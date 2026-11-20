class Solution:
    def longestPalindrome(self, s: str) -> str:
        end = len(s)
        def expand(left, right):
            while 0 <= left and right < end and left <= right and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1

        left, right = 0, 0
        for i in range(end):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i - 1, i)

            len1, len2 = r1 - l1 + 1, r2 - l2 + 1
            currMax = max(len1, len2)
            if currMax > right - left + 1:
                left, right = (l1, r1) if currMax == len1 else (l2, r2)

        return s[left:right + 1]
            
