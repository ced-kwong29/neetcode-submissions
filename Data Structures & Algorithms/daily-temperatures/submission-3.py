class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        total = len(temperatures)
        result = [0] * total

        stack = []
        for i in range(total):
            # if not stack or temperatures[stack[-1]] >= temperatures[i]:
            #     stack.append(i)
            #     continue

            while stack and temperatures[stack[-1]] < temperatures[i]:
                ndx = stack.pop()
                result[ndx] = i - ndx
            
            stack.append(i)

        return result