class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        op = []
        for i in range(n):
            j = i+1
            while j<n:
                if temperatures[i]<temperatures[j]:
                    op.append(j-i)
                    break
                else:
                    j+=1    
            if j == n:
                op.append(0)    

        return op            

