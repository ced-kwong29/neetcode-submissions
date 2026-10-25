class Solution:
    def countSubstrings(self, s: str) -> int:
        end = len(s)
        def expand(left, right):
            subCount = 0
            while 0 <= left and right < end and s[left] == s[right]:
                subCount += 1

                left -= 1
                right += 1

            return subCount

        count = 0
        for i in range(end):
            count += expand(i, i) + expand(i, i + 1)

        return count