class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        cnt = 0 
        for i in range(0,n//2):
            f = 0
            l = n-i-1
            if s[f] == s[l]:
                f+=1
                l-=1
            elif s[f] != s[l]:
                if cnt ==0:
                    f+=1
                    if s[f] != s[l]:
                        f-=1
                        l-=1
                    cnt +=1        
                else:
                    return False        
       
        return True