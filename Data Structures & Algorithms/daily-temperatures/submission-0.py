class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        end = len(temperatures)
        result = [0] * end

        stack = []
        for n in range(end):
            while stack and temperatures[stack[-1]] < temperatures[n]:
                ndx = stack.pop()
                result[ndx] = n - ndx
            stack.append(n)
        
        return result