class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        def is_valid(s):
            cnt = 0
            for ch in s:
                if ch == '(':
                    cnt +=1
                else:
                    cnt -=1
                if cnt <0:
                    return False

            return cnt == 0                

        def solve(curr):
            if len(curr) == 2*n:
                if is_valid(curr):
                    result.append(curr)
                return 

            solve(curr + '(')
            solve(curr + ')')

        solve("")
        return result            