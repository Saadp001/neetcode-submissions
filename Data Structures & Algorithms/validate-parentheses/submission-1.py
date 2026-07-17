class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ctoo = {'}':'{', ']':'[', ')':'('}

        for c in s:
            if c in ctoo:  # wheather the c is present in ctoo as a key, ex '}' if yess then its closing bracket
                if stack and stack[-1] in ctoo[c]:
                    stack.pop()

                else:
                    return False    

            else: # if no then it's an opening bracket and push into the stack
                stack.append(c)


        return  len(stack) == 0            