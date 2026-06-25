class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hm = {}

        for num in nums:
            hm[num] = 1 + hm.get(num, 0)

        ans = []

        for num, cnt in hm.items():
            if hm[num] > n//3:
                ans.append(num)
        return ans            

        