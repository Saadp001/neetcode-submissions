class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def solve(temp, visited):
            if len(temp) == len(nums):
                res.append(temp[:])
                return 
            for i in range(len(nums)):
                if i in visited:
                    continue

                if i > 0 and nums[i] == nums[i-1] and (i-1) not in visited:
                    continue
                visited.add(i)
                temp.append(nums[i])

                solve(temp, visited)

                temp.pop()
                visited.remove(i)


        solve([], set())

        return res
                  