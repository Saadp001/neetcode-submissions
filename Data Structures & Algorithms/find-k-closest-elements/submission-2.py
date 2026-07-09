class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        sorted_arr = sorted(arr, key=lambda n: abs(n - x))
        ans = sorted_arr[:k]
        return sorted(ans)