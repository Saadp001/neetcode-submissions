class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        cnt = 0 
        f = 0
        l = n-f-1        
        for f in range(0,n//2):

            if s[f] == s[l]:
                f+=1
                l-=1
            elif s[f] != s[l]:
                if cnt ==0:
                    f+=1
                    if s[f] != s[l]:
                        f-=1
                        l-=1
                        if s[f] != s[l]:
                            return False
                    cnt +=1        
                else:
                    return False        
       
        return True