class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = []

        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                ans.append(nums1[i])
                i+=1
            else:
                ans.append(nums2[j])  
                j+=1

        while i < m:
            ans.append(nums1[i])
            i+=1

        while j <n:
            ans.append(nums2[j])
            j+=1

        l = len(ans)
        mid = (l-1)//2

        if l % 2 != 0:
            return ans[mid]
        else:
            return (ans[mid]+ans[mid+1]) / 2


