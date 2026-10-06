class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        end = len(temperatures)

        result = [0] * end
        stack = []
        for ndx in range(end):
            while stack and temperatures[stack[-1]] < temperatures[ndx]:
                i = stack[-1]
                result[i] = ndx - stack.pop()

            stack.append(ndx)

        return result