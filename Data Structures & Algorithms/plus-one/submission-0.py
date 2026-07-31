class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
     

        sing = "".join(map(str, digits))

        op = int(sing)+1
        ans = []
        for i in str(op):
            ans.append(i)

        return ans    


