class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def solve(i, k, temp):
            if k ==0:
                res.append(temp[:])
                return 

            if i > n:
                return 

            temp.append(i)
            solve(i+1, k-1, temp)

            temp.pop()
            solve(i+1, k, temp)        

        
        solve(1, k, [])
        return res
