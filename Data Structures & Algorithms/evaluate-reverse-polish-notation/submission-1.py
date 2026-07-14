class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '*':
                first = stack.pop()
                second = stack.pop()
                temp = first * second
                stack.append(temp)
            elif t == '+':
                first = stack.pop()
                second = stack.pop()
                temp = first + second
                stack.append(temp)
            elif t == '-':
                first = stack.pop()
                second = stack.pop()
                temp = second - first
                stack.append(temp)
            elif t == '/':
                first = stack.pop()
                second = stack.pop()
                temp = int(second / first)
                stack.append(temp)
            else:
                stack.append(int(t))
        return stack[-1]
            

        