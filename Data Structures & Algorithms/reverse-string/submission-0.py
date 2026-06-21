class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        # i = 0
        for i in range(0,n//2):
            s[i], s[n-i-1] = s[n-i-1], s[i]



        