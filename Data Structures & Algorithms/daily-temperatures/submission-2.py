class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        end = len(temperatures)
        result = [0] * end

        stack = []
        for i in range(end):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                ndx = stack.pop()
                result[ndx] = i - ndx

            stack.append(i)

        return result

