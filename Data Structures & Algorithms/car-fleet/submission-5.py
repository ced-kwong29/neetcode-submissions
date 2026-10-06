class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for pos, rate in sorted(zip(position, speed))[::-1]:
            if not stack or (target - pos) / rate > (target - stack[-1][0]) / stack[-1][1]:
                stack.append((pos, rate))

        return len(stack)