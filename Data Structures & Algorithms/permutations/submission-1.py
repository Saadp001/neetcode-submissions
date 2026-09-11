class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def solve(temp, visited):
            if len(temp) == len(nums):
                res.append(temp[:])
                return 
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    temp.append(nums[i])

                    solve(temp, visited)

                    temp.pop()
                    visited.remove(i)


        solve([], set())

        return res
          