class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = set()

        for num in nums:
            if num in ans:
                return num
            ans.add(num)
                