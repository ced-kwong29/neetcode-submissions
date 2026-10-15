class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0

        end = len(s)
        def expand(left, right):
            while 0 <= left and right < end and s[left] == s[right]:
                self.count += 1

                left -= 1
                right += 1

        for i in range(end):
            expand(i, i)
            expand(i, i + 1)

        return self.count