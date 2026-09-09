class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def solve(i, temp, target):
            # found valid combination
            if target == 0:
                res.append(temp[:])
                return

            # dead end
            if i >= len(candidates) or target < 0:
                return

            # include current candidate (stay at same index, can reuse)
            temp.append(candidates[i])
            solve(i, temp, target - candidates[i])
            temp.pop()  # backtrack

            # skip current candidate (move to next)
            solve(i + 1, temp, target)

        solve(0, [], target)
        return res