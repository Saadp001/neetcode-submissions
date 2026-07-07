class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()

        lon = 0
        l = 0 
        r = 0     

        while r<len(s):
            if s[r] not in window:
                window.add(s[r])
                r+=1
            else:
                window.remove(s[l])
                l+=1    
            lon = max(lon, r-l)

        return lon



