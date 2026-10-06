class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key = lambda x: -x[0])

        stack = []
        for pos, rate in cars:
            if stack:
                aheadCar = stack[-1]
                time1 = (target - aheadCar[0]) / aheadCar[1]

                time2 = (target - pos) / rate
                if time2 > time1:
                    stack.append((pos, rate))
            else:
                stack.append((pos, rate))

        return len(stack)