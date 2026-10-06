class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        meom = [1, 2]
        for i in range(2, n):
            meom.append(meom[i - 2] + meom[i - 1])

        return meom[-1]