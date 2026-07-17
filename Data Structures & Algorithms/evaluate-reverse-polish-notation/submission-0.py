class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                add = stack[-1]+stack[-2]
                stack.pop()
                stack.pop()
                stack.append(add)

            elif i == '-':
                sub = stack[-2]-stack[-1]
                stack.pop()
                stack.pop()
                stack.append(sub)

            elif i== '*':
                mul = stack[-1]*stack[-2]
                stack.pop()
                stack.pop()
                stack.append(mul)   

            elif i == '/':
                div = int(stack[-2]/stack[-1])
                stack.pop()
                stack.pop()
                stack.append(div)

            else:
                stack.append(int(i))

        return stack[-1]