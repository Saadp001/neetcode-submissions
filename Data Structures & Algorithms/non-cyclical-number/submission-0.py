class Solution:
    def isHappy(self, n: int) -> bool:
        total = 0

        for digit in str(n):
            total+= int(digit)*int(digit)

        if total == 1:
            return True
        return False    
            