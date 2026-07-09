class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ans = list()
        for i in s1:
            for j in range(len(s2)):
                if i == s2[j]:
                    ans.append(j)
                    break

        
        for k in range(1,len(ans)):
            if ans[k] - 1 == ans[k-1]:
                return True           
            else:
                return False    