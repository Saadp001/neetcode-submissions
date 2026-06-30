class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        f = 0
        l = n-1

        while f < l:
            if numbers[f]+numbers[l] == target:
                return [f+1,l+1]
            
            elif numbers[f]+numbers[l] > target:
                l-=1
            else:
                f+=1

    