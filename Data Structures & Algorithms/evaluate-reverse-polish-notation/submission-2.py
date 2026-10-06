class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                add = stack.pop()
                stack[-1] += add

            elif t == "-":
                subtract = stack.pop()
                stack[-1] -= subtract
            
            elif t == "*":
                multiply = stack.pop()
                stack[-1] *= multiply

            elif t == "/":
                divide = stack.pop()
                stack[-1] = int(stack[-1] / divide)

            else:
                stack.append(int(t))

        return stack[-1]