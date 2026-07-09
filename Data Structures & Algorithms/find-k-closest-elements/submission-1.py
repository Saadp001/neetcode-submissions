class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        hm = {}
        for i in arr:
            hm[i] = abs(i-x)

        sorted_hm = dict(sorted(hm.items(), key=lambda item: item[1]))  

        ans = []
        cnt = 0
        for key in sorted_hm:
            # if len(ans) >= k:
            ans.append(key)
            cnt+=1
            if cnt >= k:
                break

        a = list(set(ans))
        a.sort()
        return a