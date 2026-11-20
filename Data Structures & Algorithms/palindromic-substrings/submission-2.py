class Solution:
    def countSubstrings(self, s: str) -> int:
        end = len(s)
        self.count = 0
        def expand(left, right):
            while 0 <= left and right < end and s[left] == s[right]:
                self.count += 1

                left -= 1
                right += 1


        for i in range(end):
            expand(i, i)
            expand(i - 1, i)

        return self.count