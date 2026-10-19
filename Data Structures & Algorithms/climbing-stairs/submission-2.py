class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        step1, step2 = 1, 2
        for i in range(2, n):
            newSteps = step1 + step2
            step1 = step2
            step2 = newSteps

        return step2