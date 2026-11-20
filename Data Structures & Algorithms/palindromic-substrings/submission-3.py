class Solution:
    def countSubstrings(self, s: str) -> int:
        end = len(s)
        def expand(left, right):
            count = 0
            while 0 <= left and right < end and s[left] == s[right]:
                count += 1

                left -= 1
                right += 1

            return count


        res = 0
        for i in range(end):
            res += expand(i, i) + expand(i - 1, i)

        return res