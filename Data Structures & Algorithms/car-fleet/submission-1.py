class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)


        stack = []
        for p, s in sorted(cars)[::-1]:
            if not stack:
                stack.append((p, s))
                continue
            
            pos, rate = stack[-1]
            if (target - p) / s > (target - pos) / rate:
                stack.append((p, s))

        return len(stack)