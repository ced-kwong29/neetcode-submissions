class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)

        stack = []
        for p, s in sorted(cars)[::-1]:
            if not stack or (target - p) / s > (target - stack[-1][0]) / stack[-1][1]:
                stack.append((p, s))

        return len(stack)