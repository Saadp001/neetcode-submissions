class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def solve(start, temp, target):
            if target == 0:
                res.append(temp[:])
                return
            if target < 0 or start >= len(candidates):
                return

            for i in range(start, len(candidates)):
                # skip duplicates at same recursion level
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                temp.append(candidates[i])
                solve(i + 1, temp, target - candidates[i])
                temp.pop()

        solve(0, [], target)
        return res