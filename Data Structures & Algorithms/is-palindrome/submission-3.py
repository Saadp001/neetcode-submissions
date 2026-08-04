class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char for char in s if char.isalnum()).lower()
        
        def rev(l , r):
            if l >= r:
                return True
            if l < r:
                if clean[l] != clean[r]:
                    return False

            return rev(l+1, r-1)            
    
            

        return rev(0, len(clean)-1)