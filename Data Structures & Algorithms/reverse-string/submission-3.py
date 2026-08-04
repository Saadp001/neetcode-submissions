class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        def rev(l, r):
            if l < r:
                rev(l+1, r-1)
                s[l], s[r] = s[r], s[l]
     

        rev(0, n-1)        
