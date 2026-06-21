class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Clean the string (alphanumeric only, lowercase)
        s_alnum_lower = "".join(char for char in s if char.isalnum()).lower()
        
        n = len(s_alnum_lower)
        
        # 2. Check characters from outside in
        for i in range(0, n // 2):
            if s_alnum_lower[i] != s_alnum_lower[n - i - 1]:
                return False  # Capital F
                
        return True  # Capital T
